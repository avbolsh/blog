from flask import redirect, url_for, render_template
from flask_login import current_user, login_user
from app.models.user import User
from app.auth import bp
from app.auth.forms import LoginForm


@bp.route("/login", methods=["GET", "POST"])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
    
    return render_template("auth/login.html", form=form)