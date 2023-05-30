from flask import Flask
from app.extension import db, migrate, Admin, ModelView

from config import Config
from .posts import posts

from app.posts import models


app = Flask(__name__)

app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)
migrate.init_app(app, db)

admin = Admin(app, name="Blog (Red Eye)", template_mode="bootstrap4")
admin.add_view(ModelView(models.Post, db.session))
admin.add_view(ModelView(models.Tag, db.session))



# Register blueprints here
app.register_blueprint(posts, url_prefix="/blog")



from app import routes

