from flask import Flask
from app.extension import db, migrate

from config import Config
#from .posts import posts

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix="/blog")

    return app



