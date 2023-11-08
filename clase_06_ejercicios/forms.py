from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    class Meta:
        locales = ['es_ES', 'es_MX', 'es']

    title = StringField("Títutlo", validators=[DataRequired(), Length(min=2, max=20)])
    genre = StringField('Género', validators=[DataRequired(), Length(min=2, max=20)])
    author = StringField("Author", validators=[DataRequired(), Length(min=2, max=20)])

