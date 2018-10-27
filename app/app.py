from flask import Flask
from flask_json import as_json
from werkzeug.contrib.fixers import ProxyFix

from app import commands, extensions
from app.config import ProdConfig


def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_errorhandlers(app)
    register_commands(app)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return app


def register_extensions(app):
    extensions.db.init_app(app)
    extensions.migrate.init_app(app, extensions.db)
    extensions.json.init_app(app)
    extensions.rq.init_app(app)


def register_errorhandlers(app):
    @as_json
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return {}, error_code

    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)


def register_commands(app):
    app.cli.add_command(commands.clean)
