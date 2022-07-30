# Karakter dizilerinde SUBSTRING (alt küme) islemleri;

# Veri yapilarindaki birimlere erismek;
hsh = "Her seyi halledecegim."
print(hsh[0])                                        # ilk terim "0" kabul edilir. 0. karakter gelir.
print(hsh[7])
print(hsh[0:3])                                      # 0. karakter dahil 3. karaktere kadar gelir.
print(hsh[:3])                                       # Ust satirdaki kodla ayni seyi ifade eder.

print(len(hsh))                                      # "len" ilk karakteri sıfır almaz.
print(hsh[10:])                                      # Alt satirla ayni, dizideki eleman sayisi cok oldugunda son terimden emin olmak icin boyle yazilabilir.
print(hsh[10:14])
print(hsh[0], hsh[6].lower())
print(hsh[0], hsh[20].upper())


# Kullanicilardan bilgi almak;
Adiniz = input()
İkinci_adiniz = input()
Yasiniz = input()
Okul = input()
Bolum = input()
Ortalama = input()
Deneyim_Yili = input()


# Alt Gorev Belirteclere "ARGUMANLAR" denir.
# Metodun basina soru isareti eklenerek ya da fonksiyonun yanina parantez acinca gorulebilir.