from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import EmailField, PasswordField, SubmitField, StringField, URLField
from wtforms.validators import DataRequired, Email, length, URL

# pip install email-validator
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = URLField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='password', validators=[DataRequired(), length(min=6)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField(label='Sign Me Up!')


class LoginForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField(label='Log In')


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
