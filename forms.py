from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    crypto_name = StringField('crypto', validators=[DataRequired()])
