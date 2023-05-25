from flask import Flask
from app.extension import db, migrate

from config import Config
from .posts import posts


app = Flask(__name__)

app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)
migrate.init_app(app, db)

# Register blueprints here
app.register_blueprint(posts, url_prefix="/blog")



from app import routes
from app.posts import models
