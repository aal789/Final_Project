from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    Username = StringField('USER_ID', validators=[DataRequired()])
    Password = StringField('PASSWORD', validators=[DataRequired()])
    submit = SubmitField('CheckStrength')
