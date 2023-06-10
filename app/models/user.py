from app import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    email = db.Column(db.String(140), nullable=False)
    passhash = db.Column(db.String(128))
    posts = db.relationship("Post", backref='author', lazy="dynamic")

    def __repr__(self):
        return f"{self.name} {self.email}" 