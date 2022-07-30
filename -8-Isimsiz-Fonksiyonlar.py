# Yan Etkili Fonksiyon : Fonksiyonun bir sekilde digaridan bagimliligi olmasi.
# Yan Etkisiz Fonksiyon : Ancak bir girdi verdigimde cıktı üretir ve cıktı her zaman aynidir.

# ISIMSIZ FONKSIYONLAR / Anonymous Function (Fonksiyona isimlendirme yapmadan, fonksiyonu kullanmak.)

# Isimlerdirme yaparak Lambda;

new_sum = lambda a, b: a + b                         # (a,b: Degiskenler, a+b: Yapilacak islem)
print(new_sum (4, 5))

# Her bir tuple icerisinde ikinci elemana gidip, kucukten buyuge siralamak istiyorum;
sirasiz_liste = [("b", 3), ("a", 8), ("d", 12), ("c", 1)]


# Isimsiz Lambda;
# Bir fonksiyon, arguman olarak kendisine basa fonksiyon alabilir (Sorted kendine arguman olarak lambdayi aldi).
sorted(sirasiz_liste, key=lambda x: x[1])           # sorted: siralama yapmak icin kullanilir.