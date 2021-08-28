from flask import Flask
from werkzeug.utils import find_modules, import_string

def register_blueprints(app):
    for name in find_modules(f"{__name__}.blueprints"):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            app.register_blueprint(mod.blueprint)

def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config or {})
    register_blueprints(app)
    return app


"""
    otra forma de generar y mantener una referencia a la app de flask.
    dentro del request se podría obtener:
        current_app.my_instance
"""
class MyApp():
    def __init__(self, config):
        self.flask_app = create_app(config)
        self.flask_app.my_instance = self
    
    def __call__(self, environ, start_response):
        return self.flask_app(environ, start_response)