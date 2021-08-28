"""
ejemplo de como manejar las conexiones y el contexto de una app flask
"""

from flask import g
from common import create_app

app = create_app()

def new_con():
    return None

def get_db():
    db = getattr(g, '_database_con', None)
    if db is None:
        ''' genero una conexión nueva y la almaceno '''
        db = g._database_con = new_con()
    return db

@app.teardown_appcontext
def close_conn(exception):
    db = getattr(g, '_database_con', None)
    if db is not None:
        db.close()



"""
ejemplo de como manejar los usuarios
"""

def get_user_from_request():
    return None

def get_user():
    user = getattr(g, 'user', None)
    if user is None:
        user = get_user_from_request()
        g.user = user
    return user