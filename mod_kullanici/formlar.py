from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginFormu(FlaskForm):

    okulno = StringField(label='Okul Numaranız', validators=[DataRequired(message='Okul No Boş Geçilemez.')])
    sifre = PasswordField(label='Şifreniz', validators=[DataRequired(message='Şifre Boş Geçilemez.')])
    beniHatirla = BooleanField(label='Beni Hatırla')
    gonder = SubmitField(label='Giriş')


def gecici():
    pass