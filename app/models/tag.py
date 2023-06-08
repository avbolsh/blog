from app import db
from app.models.common import slugify


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug=slugify(self.title)

    def __repr__(self):
        return f"<Tag id:{self.id}, title: {self.title}>"