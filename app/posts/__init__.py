from flask import Blueprint, render_template
from .models import Post

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/")
def post_list():
    posts = Post.query.all()
    return render_template("posts/post_list.html", posts=posts)  
