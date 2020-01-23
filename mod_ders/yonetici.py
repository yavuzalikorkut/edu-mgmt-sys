from flask import Blueprint, render_template, url_for, redirect, request, abort, jsonify
from .model import *
from .formlar import DersFormu
from flask_login import login_required

mod_ders = Blueprint('ders', __name__)


@mod_ders.route('/liste/<int:limit>/<int:offset>')
@mod_ders.route('/')
@login_required
def dersListe(limit=10, offset=0):
    dersler = Ders.query.limit(limit).offset(offset).all()
    kayitSayisi = db.session.query(db.func.count(Ders.id)).scalar()
    ilkSayfaBilgileri = {
        'link': url_for('ders.dersListe', limit=limit, offset=0)
    }
    oncekiSayfaBilgileri = {
        'link': url_for('ders.dersListe', limit=limit, offset=max(0, offset - limit))
    }
    sonrakiSayfaBilgileri = {
        'link': url_for('ders.dersListe', limit=limit, offset=min(kayitSayisi - 1, offset + limit))
    }
    sonSayfaBilgileri = {
        'link': url_for('ders.dersListe', limit=limit, offset=kayitSayisi - 1)
    }
    return render_template('dersler/liste.html',
                           veri=dersler,
                           ilkSayfa=ilkSayfaBilgileri,
                           oncekiSayfa=oncekiSayfaBilgileri,
                           sonrakiSayfa=sonrakiSayfaBilgileri,
                           sonSayfa=sonSayfaBilgileri)


@mod_ders.route("/ekle", methods=["GET", "POST"])
@login_required
def dersEkle():
    form = DersFormu()
    if form.validate_on_submit():
        yeniDers = Ders()
        yeniDers.dersAdi = form.dersAdi.data
        yeniDers.dersKodu = form.dersKodu.data
        yeniDers.kredi = form.kredi.data
        yeniDers.ogretimGorevlisi = form.ogretimGorevlisi.data
        db.session.add(yeniDers)
        db.session.commit()
        return redirect(url_for('ders.dersListe'))
    # Boş formu gösterelim.
    return render_template('dersler/ekle.html',
                           form=form,sayfa_baslik="Yeni Ders Ekle")


@mod_ders.route("/sil", methods=['POST'])
@login_required
def dersSil():
    dersId = request.form["id"]

    silinecekDers = Ders.query.filter(Ders.id == dersId).one_or_none()

    if silinecekDers is None:
        abort(404)

    db.session.delete(silinecekDers)
    db.session.commit()

    return jsonify({'sonuc': 'TAMAM'})


@mod_ders.route("/duzenle/<int:id>", methods=["GET", "POST"])
@login_required
def dersDuzenle(id):
    duzenlenecekDers = Ders.query.filter(Ders.id == id).one_or_none()

    if duzenlenecekDers is None:
        abort(404)

    form = DersFormu()
    if form.validate_on_submit():
        # Bu kısım her şey yolunda düzenleme tamamsa çalışacak.
        duzenlenecekDers.dersAdi = form.dersAdi.data
        duzenlenecekDers.dersKodu = form.dersKodu.data
        duzenlenecekDers.kredi = form.kredi.data
        duzenlenecekDers.ogretimGorevlisi = form.ogretimGorevlisi.data
        db.session.commit()
        return redirect(url_for('ders.dersListe'))

    # Burası ya ilk kez form gösterileceğinde ya da hata olduğunda çalışacak
    form.dersKodu.data = duzenlenecekDers.dersKodu
    form.dersAdi.data = duzenlenecekDers.dersAdi
    form.kredi.data = duzenlenecekDers.kredi
    form.ogretimGorevlisi.data = duzenlenecekDers.ogretimGorevlisi

    # Dolu formu gösterelim.
    return render_template('dersler/ekle.html',
                           form=form,
                           sayfa_baslik="{} Dersini Düzenle".format(duzenlenecekDers.dersAdi))
