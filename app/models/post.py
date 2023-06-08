from datetime import datetime
from time import time
from app import db
from app.models.common import slugify


posts_tags = db.Table("posts_tags", 
                      db.Column("post_id", 
                                db.Integer, 
                                db.ForeignKey("post.id")), 
                      db.Column("tag_id", 
                                db.Integer, 
                                db.ForeignKey("tag.id")))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    tags = db.relationship("Tag", secondary=posts_tags, backref=db.backref("posts"), lazy="dynamic")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))

    def __repr__(self):
        return f"<Post id: {self.id}, title: {self.title}>"