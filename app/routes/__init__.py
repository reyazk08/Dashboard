from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

from .dashboard import *
from .historical import *
from .control import *
from .system import *