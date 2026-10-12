# Kapsam (Scope) Analizi ve Örnekleri

### 1. Global Değişken Okuma
```python
x = 10
def oku():
    print(x)
oku()
```
* **Tahmin:** 10 yazdırır.
* **Gerçek Sonuç:** 10
* **Neden:** Python bir değişkeni yerel kapsamda (local scope) bulamazsa LEGB kuralına göre sırasıyla Enclosing, Global ve Built-in kapsamlara bakar. Global alanda tanımlı olduğu için sorunsuz okunur.

---

### 2. UnboundLocalError Örneği
```python
sayac = 0
def arttir():
    sayac = sayac + 1
arttir()
```
* **Tahmin:** UnboundLocalError hatası verir.
* **Gerçek Sonuç:** `UnboundLocalError: cannot access local variable 'sayac' where it is not associated with a value`
* **Neden:** Fonksiyon gövdesi içinde `sayac = ...` şeklinde bir atama yapıldığı anda Python derleme aşamasında `sayac` değişkenini yerel (local) değişken olarak işaretler. Sağ taraftaki `sayac + 1` ifadesini hesaplarken yerel değişkene henüz değer atanmadığını görür ve bu hatayı fırlatır.
* **Çözüm:** Fonksiyonun içine ya `global sayac` eklenmelidir ya da değişken fonksiyona argüman olarak iletilip döndürülmelidir (Pure function yaklaşımı).

---

### 3. İç İçe Fonksiyon ve Closure (nonlocal)
```python
def dis_fonksiyon():
    deger = 5
    def ic_fonksiyon():
        nonlocal deger
        deger += 1
        return deger
    return ic_fonksiyon
```
* **Tahmin:** `ic_fonksiyon` her çağrıldığında `deger` 1 artar (6, 7, 8...).
* **Gerçek Sonuç:** 6, 7, 8...
* **Neden:** `nonlocal` anahtar kelimesi, Python'a bu değişkenin en yakın dış fonksiyon kapsamında (enclosing scope) aranması gerektiğini bildirir. Böylece iç fonksiyon dış fonksiyonun durumunu hafızasında saklar (Closure).
