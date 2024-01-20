from flask import Response, jsonify, make_response

class APIResponse(Response):
    @classmethod
    def respond(cls, data=None, message=None, status_code=200):
        response_data = {'data': data, 'message': message}
        return make_response(jsonify(response_data), status_code)

    @classmethod
    def respond_error(cls, message, status_code):
        return cls.respond(message=message, status_code=status_code)
