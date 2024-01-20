from flask import Blueprint,abort
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, AssignmentStateEnum

from .schema import AssignmentSchema,AssignmentGradeSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

# @principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
# @decorators.authenticate_principal
# def list_assignments_for_principal(p):
#     """List all submitted and graded assignments for the principal."""
#     assignments_for_principal = Assignment.get_assignments_for_principal(principal_id=p.principal_id)
#     assignments_dump = AssignmentSchema().dump(assignments_for_principal, many=True)
#     return APIResponse.respond(data=assignments_dump)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_all_assignments(p):
    """Returns list of all submitted and graded assignments"""
    all_assignments = Assignment.get_assignments_submitted_and_graded()
    all_assignments_dump = AssignmentSchema().dump(all_assignments, many=True)
    return APIResponse.respond(data=all_assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment_by_principal(p, incoming_payload):
    """Grade or re-grade an assignment by a principal"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    # Retrieve the assignment by ID
    assignment = Assignment.get_by_id(grade_assignment_payload.id)

    # Ensure the assignment exists
    if assignment is None:
        return APIResponse.respond_error(message='Assignment not found', status_code=404)

    # Check if the assignment is in Draft state
    if assignment.state == AssignmentStateEnum.DRAFT:
        return APIResponse.respond_error(message='Cannot grade a draft assignment', status_code=400)
    if assignment.state != AssignmentStateEnum.DRAFT:
    # Grade the assignment
        assignment.grade = grade_assignment_payload.grade
        assignment.state = AssignmentStateEnum.GRADED
        db.session.commit()

    # Dump the graded assignment data
    graded_assignment_dump = AssignmentSchema().dump(assignment)
    
    return APIResponse.respond(data=graded_assignment_dump, status_code=200)  # Adjust the status code as needed
