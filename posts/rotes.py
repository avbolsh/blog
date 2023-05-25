from posts import posts
from flask import render_template, abort
from jinja2 import TemplateNotFound


@posts.route("/")
def post_list():
    try:
        return render_template("post_list.html")
    except TemplateNotFound:
        abort(404)


