from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user
from .formlar import LoginFormu
from .model import *

mod_kullanici = Blueprint('kullanici', __name__)


@mod_kullanici.route('/login', methods=['post', 'get'])
@mod_kullanici.route('/', methods=['post', 'get'])
def kullaniciLogin():
    loginForm = LoginFormu()
    if loginForm.validate_on_submit():
        kullanici = Kullanici.query.filter(Kullanici.kullaniciadi == loginForm.okulno.data).one_or_none()
        if kullanici is None:
            return render_template('login.html', form=loginForm, hata="Kullanıcı adı veya şifre hatalı")
        if kullanici.sifreDogrula(loginForm.sifre.data):
            login_user(kullanici)
            return redirect(url_for('ders.dersListe'))
        else:
            return render_template('login.html', form=loginForm, hata="Kullanıcı adı veya şifre hatalı")
    return render_template('login.html', form=loginForm, hata="")


@mod_kullanici.route('/cikis')
def cikis():
    logout_user()
    return redirect(url_for('kullanici.kullaniciLogin'))


def ok():
    return "OK"