from flask import Blueprint, render_template, redirect, url_for
from .models import Post, Tag
from flask import request
from .forms import PostForm
from app import db

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/create/", methods=["GET", "POST"])
def post_create():
    
    form = PostForm()

    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            pass
    else:
        return render_template("posts/post_create.html", form=form)
    
    return redirect(url_for("index"))


@posts.route("/")
def post_list():
    q = request.args.get("q")

    if q:
        posts = Post.query.filter(Post.title.contains(q) | 
                                  Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    page = request.args.get("page")

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    
    pages = posts.paginate(page=page, per_page=2)
    
    return render_template("posts/post_list.html", posts=posts, pages=pages)


@posts.route("/<slug>/")
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()  
    return render_template("posts/post_detail.html", post=post)


@posts.route('/tags/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    return render_template("posts/tag_detail.html", tag=tag)