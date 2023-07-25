from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class WeatherForm(FlaskForm):
    # country = StringField(label="Country", validators=[DataRequired()])
    city = StringField(label="City", validators=[DataRequired()])
    submit = SubmitField(label="Show Weather")


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
    last_page = HiddenField()

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=6, max=30)])
    email_address = StringField(label="Email Address", validators=[DataRequired(), Email()])
    country = StringField(label="Country", validators=[DataRequired()])
    city = StringField(label="City", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=8), DataRequired()])
    password_confirm = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Sign in")
