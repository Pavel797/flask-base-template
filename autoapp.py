from flask.helpers import get_debug_flag

from app.app import create_app
from app.config import DevConfig, ProdConfig


Config = DevConfig if get_debug_flag() else ProdConfig
app = create_app(Config)
