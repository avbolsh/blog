from flask import Blueprint, render_template
from .models import Post, Tag
from flask import request

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/")
def post_list():
    q = request.args.get("q")

    if q:
        posts = Post.query.filter(Post.title.contains(q) | 
                                  Post.body.contains(q))
    else:
        posts = Post.query.all()
    
    return render_template("posts/post_list.html", posts=posts)


@posts.route("/<slug>/")
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()  
    return render_template("posts/post_detail.html", post=post)


@posts.route('/tags/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    return render_template("posts/tag_detail.html", tag=tag)