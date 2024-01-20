from marshmallow import Schema, fields

class TeacherSchema(Schema):    
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        strict = True
