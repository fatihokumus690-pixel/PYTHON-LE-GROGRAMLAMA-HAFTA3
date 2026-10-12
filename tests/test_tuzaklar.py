import pytest


def test_varsayilan_arguman_tuzagi():
    """Mutable default argument (değiştirilebilir varsayılan argüman) tuzağını gösterir."""
    def hatali_yakit_ekle(miktar: int, depo: list = []):
        depo.append(miktar)
        return depo

    d1 = hatali_yakit_ekle(10)
    d2 = hatali_yakit_ekle(20)

    # İkinci çağrıda depo sıfırlanmaz, 10'un yanına 20 eklenir:
    assert d2 == [10, 20]
    assert d1 is d2  # Aynı liste referansını paylaşırlar


def test_yakit_ekle_none_kalibi_cozumu():
    """None kalıbı (Sentinel) ile düzeltilmiş güvenli fonksiyon testi."""
    def duzgun_yakit_ekle(miktar: int, depo: list | None = None) -> list:
        if depo is None:
            depo = []
        depo.append(miktar)
        return depo

    depo1 = duzgun_yakit_ekle(10)
    depo2 = duzgun_yakit_ekle(20)

    assert depo1 == [10]
    assert depo2 == [20]
    assert depo1 is not depo2
