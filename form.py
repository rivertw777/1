from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

#회원가입 폼
class SignupForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired()])
    user_pw = PasswordField('user_pw', validators=[DataRequired(), EqualTo('re_pw')])
    re_pw = PasswordField('re_pw', validators=[DataRequired()])

#로그인 폼
class LoginForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired()])
    user_pw = PasswordField('user_pw', validators=[DataRequired()])

#커피박 수거량 입력폼
class MileageForm(FlaskForm):
    mileage= StringField('mileage',  validators=[DataRequired()])
