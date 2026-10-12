import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu, galaksi_kur
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler


def test_envanter_metni_var():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_yok():
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu():
    beklenen = "Nereye gitmek istersin?\n[1] centauri [2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen


def test_galaksi_kur_basarili():
    gezegenler = ["dünya", "mars"]
    baglantilar = {"dünya": ["mars"], "mars": ["dünya"]}
    sonuc = galaksi_kur(gezegenler, baglantilar, "dünya", yakit=80)
    assert sonuc["konum"] == "dünya"
    assert sonuc["yakit"] == 80


def test_galaksi_kur_hatali_baslangic():
    with pytest.raises(ValueError):
        galaksi_kur(["dünya"], {"dünya": []}, "neptun")


def test_hamle_sayaci():
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3


def test_en_bagli_gezegenler():
    galaksi = {
        "gezegenler": ["a", "b", "c"],
        "baglantilar": {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"],
        },
    }
    # b: 2 bağlantı, a ve c: 1 bağlantı (eşitlikte alfabetik: a önce gelir)
    assert en_bagli_gezegenler(galaksi) == ["b", "a", "c"]
