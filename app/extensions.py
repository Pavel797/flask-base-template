from flask_json import FlaskJSON
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_rq2 import RQ


json = FlaskJSON()
db = SQLAlchemy()
migrate = Migrate()
rq = RQ()
