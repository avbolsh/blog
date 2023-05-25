from flask import Flask
from config import Config
from posts import posts


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(posts, url_prefix="/blog")

from app import routes
