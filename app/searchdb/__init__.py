from flask import Blueprint

searchdb = Blueprint('searchdb', __name__)

from . import views