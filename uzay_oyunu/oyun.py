import json
from pathlib import Path
from uzay_oyunu.araclar import hamle_sayaci


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Eşya durumuna göre envanter metni oluşturur. (Görev 1)"""
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hiperdrive")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandırılmış tek satır menü olarak döndürür. (Görev 1)"""
    menu_ogeleri = [f"[{i}] {hedef}" for i, hedef in enumerate(hedefler, 1)]
    return f"Nereye gitmek istersin?\n{' '.join(menu_ogeleri)}"


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: int,
) -> dict:
    """Galaksi verilerini doğrular ve oyun durumunu döndürür. (Görev 3)"""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok!")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def travel(galaksi: dict) -> None:
    """Oyunun ana döngüsü."""
    sayac = hamle_sayaci()
    mevcut = galaksi["konum"]
    hedefler = galaksi["baglantilar"][mevcut]

    print(f"\nŞu an: {mevcut.upper()}")
    print(envanter_metni(True, False, True))
    print(hedef_menusu(hedefler))

    # Örnek adım
    hamle = sayac()
    print(f"Oyunu {hamle} hamlede bitirdin!")


if __name__ == "__main__":
    veri_yolu = Path(__file__).parent / "galaksi.json"
    with open(veri_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)

    oyun_durumu = galaksi_kur(**veri)
    travel(oyun_durumu)
