from flask import Blueprint

posts = Blueprint("posts", __name__, "templates")

from posts import rotes