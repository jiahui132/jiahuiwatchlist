from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, MultipleFileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from flask_ckeditor import CKEditorField



class MyBaseForm(FlaskForm):
    class Meta:
        locals = ['zh']


class LoginForm(MyBaseForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')


class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()


class MultiUploadForm(FlaskForm):
    photo = MultipleFileField('Upload Image', validators=[DataRequired()])
    submit = SubmitField()


class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    save = SubmitField('Save')
    publish = SubmitField('Publish')


class SigninForm(FlaskForm):
    username = StringField('Usename', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Passwrod', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    username = StringField('Usename', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Passwrod', validators=[DataRequired(), Length(8, 128)])
    submit = SubmitField('Register')