from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name="Blog", template_mode="bootstrap4")