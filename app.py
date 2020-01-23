from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ÇOK GİZLİ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bys.ktu'

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
login = LoginManager(app)

from mod_ders.yonetici import mod_ders
from mod_kullanici.yonetici import mod_kullanici

migrate = Migrate(app, db)

app.register_blueprint(mod_ders, url_prefix='/ders')
app.register_blueprint(mod_kullanici, url_prefix='/kullanici')
app.register_blueprint(mod_kullanici, url_prefix='/')

login.login_view = "kullanici.kullaniciLogin"

if __name__ == '__main__':
    app.run()
