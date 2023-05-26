from wtforms import Form, StringField, TextAreaField, SubmitField


class PostForm(Form):
    title = StringField("Title")
    body = TextAreaField("Body")
    submit = SubmitField("Create")
    