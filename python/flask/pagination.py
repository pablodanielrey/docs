"""
Ejemplo de paginación dentro de la cabecera link
"""

from flask import Flask, json, Response, request
from werkzeug.urls import url_join

class PaginatedApiResult():
    def __init__(self, value, status=200, next_page=None):
        self.value = value
        self.status = status
        self.next_page = next_page

    def to_response(self):
        rv = Response(json.dumps(self.value), status=self.status, mimetype='application/json')
        if self.next_page is not None:
            rv.headers['Link'] = f"{url_join(request.url, self.next_page)}; rel=\"next\""
        return rv

