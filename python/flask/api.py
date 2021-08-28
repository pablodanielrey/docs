"""
Ejemplo de como manejar apis en flask de una forma consistente
"""

from flask import Flask, json, Response

class ApiResult():
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value), status=self.status, mimetype='application/json')


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message}, status=self.status)


def register_error_handlers(app):
    app.register_error_handler(ApiException, lambda err: err.to_result())


"""
Ejemplo de la app de flask que sería ya la api.
"""
class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)