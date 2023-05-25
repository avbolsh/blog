from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from .posts import posts


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(posts, url_prefix="/blog")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.posts import models
