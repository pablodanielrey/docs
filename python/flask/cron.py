from common import create_app
from werkzeug.utils import import_string

def run_cron(import_name, config):
    func = import_string(import_name)
    app = create_app(config=config)
    with app.app_context():
        func()