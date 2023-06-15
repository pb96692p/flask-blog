from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',
                            validators=[DataRequired(),
                             Length(min=2, max=20)])

    email = StringField('Email',
                            validators=[DataRequired(),
                             Email()])
    
    password = PasswordField('Password',
                            validators=[DataRequired()
                            ])
    
    confirm_password = PasswordField('Comfirm Password',
                            validators=[DataRequired(),
                            EqualTo('password')
                            ])
    submit = SubmitField('sigh up')

