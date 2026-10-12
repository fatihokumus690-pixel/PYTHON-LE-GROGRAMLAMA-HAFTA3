import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında 1 artan bir sayaç fonksiyonu döndürür (Closure). (Görev 5)"""
    sayac = 0

    def sayac_artir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return sayac_artir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla sıralar. (Görev 5)"""
    gezegenler: list[str] = galaksi["gezegenler"]
    baglantilar: dict[str, list[str]] = galaksi["baglantilar"]

    # -len(...) azalan sıralama, x ise alfabetik artan sıralama sağlar
    return sorted(gezegenler, key=lambda x: (-len(baglantilar.get(x, [])), x))


def sure_olc(fonksiyon: Callable) -> Callable:
    """Bir fonksiyonun çalışma süresini ölçen decorator / sarmalayıcı. (Bonus)"""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.6f} saniye sürdü.")
        return sonuc

    return wrapper


if __name__ == "__main__":
    ornek_galaksi = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["dünya", "kara_delik"],
            "orion": ["centauri", "kara_delik"],
            "kara_delik": ["sirius", "orion"],
        },
    }
    olculen_en_bagli = sure_olc(en_bagli_gezegenler)
    print("Sıralama:", olculen_en_bagli(ornek_galaksi))
