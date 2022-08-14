from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


class RegisterForm(FlaskForm):
    user_id = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "user_id"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "password"})
    
    submit = SubmitField("Register")

class RegisterForm(FlaskForm):
    user_id = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "user_id"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "password"})
    
    submit = SubmitField("Register")
    
