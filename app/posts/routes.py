from flask import render_template, request, redirect, url_for
from app.posts import bp
from app.posts.forms import PostForm
from app.models.post import Post
from app.models.tag import Tag
from app import db


@bp.route("/create/", methods=["GET", "POST"])
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
    
    return redirect(url_for("main.index"))


@bp.route("/")
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


@bp.route("/<slug>/")
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()  
    return render_template("posts/post_detail.html", post=post)


@bp.route('/tags/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    return render_template("posts/tag_detail.html", tag=tag)


@bp.route('/<slug>/edit', methods=["POST", "GET"])
def post_update(slug):
    
    post = Post.query.filter(Post.slug==slug).first()
    
    if request.method == "POST":
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for("posts.post_detail", slug=post.slug))

    form = PostForm(obj=post)        
    return render_template('posts/post_edit.html', post=post, form=form)
        