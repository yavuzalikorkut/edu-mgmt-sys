from app import db


class Ders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dersKodu = db.Column(db.String(50))
    dersAdi = db.Column(db.String(255))
    kredi = db.Column(db.Integer)
    ogretimGorevlisi = db.Column(db.String(255))
