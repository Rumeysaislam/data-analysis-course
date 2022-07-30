# String metodlari / "len" metodu (Eleman sayisi bilgisine ulasmak icin);

pwr = "power"                                     # Kelimelerin basindaki tirnak isaretini unutma!
print(pwr)
print(len(pwr))
print(len("power"))

print(len("Her seyi halledecegim."))              # Noktalama isaretleri ve bosluklari da sayar.
print(len("Her_seyi*halledecegim."))


# String metodlari / "upper" - "lover" metodlari (Buyuk-kucuk harf donusumleri);
pwr = "power"
print(pwr.upper())                               # Tum harfleri buyuk harfle yazmak icin
print(pwr.lower())                               # Tum harfleri kucuk harfle yazmak icin

print(pwr.islower())                             # Tum harfler kucuk harf mi?
print(pwr.isupper())                             # Tum harfler buyuk harf mi?


# String metodları / "replace" metodu (Karakter degistirme);
print(pwr.replace("o", "a"))
print(pwr.replace("we", "an"))                   # Kalici olarak degistirmek icin yeni atama yapman gerekiyor!


# "strip" metodu (Karakter ve bosluk) kirpma islemi (bastan ve sondan);
hsh = "* Her seyi halledecegim. *"
print(hsh)
hsh.strip()
print(hsh.strip("*"))

hsh = " Her seyi helledecegim. "
print(hsh.strip())

hsh = " Her seyi halledecegim "
hsh.strip()
print(hsh.strip())

hsh = " * Her seyi halledecegim *  "
hsh.strip(" * ")
print(hsh.strip(" * "))

hsh = "&Her seyi halledecegim&"
hsh.strip("&")
print(hsh.strip("&"))

hsh = "***Her seyi halledecegim***"
hsh.strip("*")
print(hsh.strip("*"))

hsh = "//Her seyi halledecegim"
hsh.strip("//")
print(hsh.strip("//"))


# Uygulanabilecek metodlari görmek icin "dir" metodu;
pwr = "power"
print(type(pwr))
dir(pwr)

sayı = 32
print(type(32))
dir(sayı)