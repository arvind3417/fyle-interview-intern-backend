from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers_for_principal(p):
    """List all teachers."""
    all_teachers = Teacher.get_all_teachers()
    
    teachers_dump = [
        {
            "id": teacher.id,
            "created_at": teacher.created_at,
            "updated_at": teacher.updated_at,
            "user_id": teacher.user_id  # Add other necessary fields
        }
        for teacher in all_teachers
    ]

    return APIResponse.respond(data=teachers_dump)
