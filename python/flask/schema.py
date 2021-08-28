"""
ejemplo de como validar los parámetros usando jsonschema
"""

from functools import update_wrapper
from flask import request
from voluptuous import Invalid
from api import ApiException, ApiResult


def dataschema(schema):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(request.get_son()))
            except Invalid as e:
                raise ApiException(f'Invalid data {e.msg} {e.path}')
            return f(*args, **kwargs)
        return update_wrapper(new_func, f)
    return decorator



"""
ejemplo de uso en una ruta de flask
"""
from voluptuous import Schema, REMOVE_EXTRA

#@app.route('/add', methods=[POST])
@dataschema(Schema({
        'a': int,
        'b': str
    }, extra=REMOVE_EXTRA))
def ruta_de_flask(a, b):
    return ApiResult({'resultado': f'el número {a} y el string {b}'})