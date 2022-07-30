### VERI YAPILARI

## 1) Liste Olusturma;
liste = ["a", 19.3, 30]
liste_iki = [1, 2, 3, 4, 5]
tum_liste = [liste, liste_iki]

print(len(liste))
print(len(liste_iki))

print(liste[2])
print(liste_iki[3])
type(liste[2])                                  # Liste icindeki bir elemanin turu

print(tum_liste)
len(tum_liste)

print(tum_liste[1])
type(tum_liste[1])

print(tum_liste[1][2])                          # Liste icindeki listenin elemanina ulasmak icin!

# Listelere eleman EKLEME / DEGISTIRME / SILME

# Eleman Degistirme;
liste = ["anil", "rumeysa", "tilda"]
liste[2] = "defne"
print(liste)

liste = ["anil", "rumeysa", "tilda"]
liste[0:2] = "hakan", "melda"                   # Sifirdan iki'ye kadar degisiklik yani 0. ve 1. terim degisecek.)
print(liste)


# Eleman Ekleme;
liste = ["anil", "rumeysa", "tilda"]
print(liste + ["defne"])                        # Kalici bir ekleme olmasini istiyorsan yeni liste tanımla.

liste = ["anil", "rumeysa", "tilda"]
liste = liste + ["defne"]
print(liste)


# Eleman Silme;
liste = ["anil", "rumeysa", "tilda", "defne"]
del liste[3]
print(liste)


# METODLAR ile Listelere eleman EKLEME / SILME

# "apppend" metodu / Ekleme;
liste = ["anil", "rumeysa", "tilda"]
liste.append("defne")
print(liste)


# "remove" metodu / Silme;
liste = ["anil", "rumeysa", "tilda", "defne"]
liste.remove("defne")
print(liste)


# INDEXLERE göre Listelere eleman EKLEME / SİLME

# "insert" metodu;
liste = ["anil", "rumeysa", "tilda"]
liste.insert(1, "hakan")                            # Değişiklik kalıcı değil, 1. elemana ekleme yaptim.
print(liste)


# Listenin en sonuda eklemek icin;
liste = ["anil", "rumeysa", "tilda"]
liste.insert(len(liste), "defne")
print(liste)


# "pop" metodu;
liste = ["anil", "hakan", " rumeysa", "tilda"]
liste.pop(1)
print(liste)


# Diger Liste metodlari

# "count" / Sayma Metodu;
liste = ["anil", "hakan", " rumeysa", "tilda"]
liste.count("hakan")

# "copy" / Kopyalama Metodu (Mevcut listeyi kopyalamak icin kullanilir.);
liste = ["anil", "rumeysa", "tilda"]
liste_yedek = liste.copy()
print(liste_yedek)


# "extend" metodu (iki listeyi birlestirmek icin kullanilir.);
liste = ["anil", "rumeysa", "tilda"]
liste.extend(["hakan", "melda", "defne"])
print(liste)

liste = ["anil", "rumeysa", "tilda"]
liste2 = ["hakan", "melda", "defne"]
liste.extend(liste2)
print(liste)


# "index" metodu (Bir elemanin hangi indexte oldugunu bulma metodu);
liste = ["anil", "rumeysa", "tilda"]
liste.index("anıl")


# "reverse" metodu (listeyi ters cevirme);
liste = ["anil", "rumeysa", "tilda"]
liste.reverse()
print(liste)

liste = ["anil", "rumeysa", "tilda"]
liste2 = ["hakan", "melda", "defne"]
liste.extend(liste2)
liste.reverse()
print(liste)


# "sort" metodu (sayilarda siralama);
liste_sayilar = [16, 12, 2020]
liste_sayilar.sort()
print(liste_sayilar)

liste_sayilar = [3, 16, 5, 12, 7, 13, 650, 200, 2020]
liste_sayilar.sort()
print(liste_sayilar)


# "clear" / Silme Metodu;
liste_sayilar = [16, 12, 2020]
liste_sayilar.clear()
print(liste_sayilar)



## 2) Tuple Olusturma (tupleler "SABIT VERİ YAPILARI" dir ve DEGISTIRELEMEZLER.);

t = ("anil", "rumeysa", "tilda", 16, 12, 2020)
type(t)

t = ("anil")
type(t)                                             # Tek nesne olunca sonuna virgul koyulmazsa tipini str sanar.

t = ("anil",)
print(type(t))


# Erisim islemi;
t = ("anil", "rumeysa", "tilda", 16, 12, 2020)
print(t[4])                                         # DEGISIM ISLEMI YAPILAMAZ!


## 3) Dictionary Olusturma (key - value ikisi de hem str hem int olabilir.);

sozluk = {"REG": "Regrasyon Modeli",
          "LOJ": "Lojistik Regrasyon",
          "CART": "Classification and Reg."}
print(len(sozluk))


# value'lar iki ya da daha fazla degere de karsilik gelebilirler;
sozluk = {"REG": ["RMS", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}
print(len(sozluk))


# Icerisindeki elemana ulasma;
print(sozluk["REG"])


# Sozluk icerisinde sozluk olusturma ve icerisindeki elemana ulasma;
sozluk = {"REG": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},
          "LOJ": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30}}

print(sozluk["REG"]["SSE"])


# Dictionaryde EKLEME ve DEGISTIRME;
sozluk = {"REG": "Regrasyon Modeli",
          "LOJ": "Lojistik Regrasyon",
          "CART": "Classification and Reg."}
sozluk["GBM"] = "Gradient Boosting Mac."              # key ile birlikte ekleme
print(sozluk)


# Var olan key degeri yakalanip atama islemi yapilarak degisiklik yapilir;
sozluk = {"REG": "Regrasyon Modeli",
          "LOJ": "Lojistik Regrasyon",
          "CART": "Classification and Reg."}
sozluk["REG"] = "Çoklu Doğrusal Regresyon"          # "=" işaretine dikkat et!
print(sozluk)


# Key'ler sadece sabit veri yapilariyla olusturulur;
# str, int, tuple (listeler, sabit veri yapisi olmadigindan key olamazlar. Valueler icin bu durum soz konusu degil)



## 4) SET (Kume) Olusturma;

# Liste uzerinden set olusturma;
liste = [1, "r", "rumeysa", 123]
print(set(liste))


# Tuple uzerinden set olusturma;
t = (1, "r", "rumeysa", 123,)
print(set(t))

# Essizlik ozelligi;
rhsh = "rumeysa_her_seyi_halledecek."
print(set(rhsh))
s = set(rhsh)
print(len(rhsh))
print(len(s))

# Setler sirasizdir, index islemlerini desteklemez.


# Setlerden elemen EKLEME / CIKARMA;
rhsh = "rumeysa", "halledecek."
s = set(rhsh)


# "add" / Ekleme metodu;
s.add("her seyi")
print(s)


# "remove" / Cikarma metodu;
rhsh = "rumeysa", "her seyi", "halledecek"
s = set(rhsh)

s.remove("her seyi")
print(s)

s.remove(
    "her seyi")                 # Keyerror verdi. Cünkü; daha önce silmistim, sildigimden emin olup hata almamak icin kaldirma islemini "discard" ile yaparim.
print(s)

rhsh = "rumeysa", "her seyi", "halledecek"
s = set(rhsh)
s.remove("her seyi")
print(s)
s.discard("her seyi")           # Silecek bir sey bulmadi ama yine de uyari vermedi!
print(s)


# SETLERDE FARK ISLEMLERİ

# Fark: difference() or "-"
# Kesisim: intersection() or "&"
# Birlesim: union()
# Birbirinde olmayanlar: symmetric_difference()

set1 = set([1, 3, 5])           # Listeden set olusturduk.
set2 = set([1, 2, ])

print(set1 - set2)              # set1'de olup set2'de olmayan elemanlar
print(set1.difference(set2))

print(set2 - set1)              # set2'de olup set1'de olmayan elemanlar
print(set2.difference(set1))

print(set1 & set2)
print(set1.intersection(set2))  # Tanimlama yapmadikca kalici olmaz.
kesişim = set1.intersection(set2)
print(kesişim)

print(set1.union(set2))         # Birlesim
print(set2.union(set1))

union = set1.union(set2)        # Her bir eleman bir defa alinir.
print(union)


# Kesişimden yeni eleman olusturma;
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
set1.intersection_update(set2)
print(set1)


# Setlerde Sorgu Islemi;
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
set1.isdisjoint(set2)           # Kesisim bos mu?


set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
set1.issubset(set2)             # set1, set2'nin alt kumesi mi?


set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
set1.issuperset(set2)           # Set1, Set2'yi kapsiyor mu?


# Liste'ler: Degistirilebilir, Sirali, Kapsayici
# Tuple'lar: Degistirilemez, Sirali, Kapsayici
# Sozluk: Degistirilebilir, Sirali, Kapsayici,
# Set'ler: Degistirilebilir, Sirasiz-Essiz, Kapsayici