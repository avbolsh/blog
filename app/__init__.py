from flask import Flask
from app.extension import db, migrate, admin, ModelView 

from config import Config
from app.models.post import Post
from app.models.tag import Tag
from app.models.user import User

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    admin.init_app(app)
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Tag, db.session))
    admin.add_view(ModelView(User, db.session))


    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix="/blog")

    return app



