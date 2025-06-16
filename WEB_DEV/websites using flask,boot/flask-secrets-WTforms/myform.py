from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, length

# pip install email-validator

class MyForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField(label='log In')
