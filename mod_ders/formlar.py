from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DersFormu(FlaskForm):
    dersKodu = StringField(label="Ders Kodu", validators=[DataRequired(message="Ders Kodu boş geçilemez")])
    dersAdi = StringField(label="Ders Adı", validators=[DataRequired(message="Ders Adı boş geçilemez")])
    kredi = IntegerField(label="Ders Kredisi", validators=[DataRequired(message="Ders Kredisi Boş Geçilemez")])
    ogretimGorevlisi = StringField(label="Öğretim Görevlisi",
                                   validators=[DataRequired(message="Öğretim Görevlisi boş geçilemez")])
    kaydet = SubmitField(label="Kaydet")
