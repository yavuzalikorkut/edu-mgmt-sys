from app import db, login
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash


class Kullanici(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    kullaniciadi = db.Column(db.String(255))
    sifre = db.Column(db.String(255))

    def sifreBelirle(self, yeniSifre):
        self.sifre = generate_password_hash(yeniSifre)

    def sifreDogrula(self, yeniSifre):
        return check_password_hash(self.sifre, yeniSifre)


@login.user_loader
def kullaniciYukle(id):
    return Kullanici.query.filter(Kullanici.id==id).one_or_none()