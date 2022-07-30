
# Mini Uygulama

limit = 50000

store_name = input("Magaza Adi Giriniz:")
store_gelir = int(input("Geliri Yaziniz:"))                              # str olarak girilen sayısal veriyi int cevirdik!

if store_gelir > limit:
    print("TEBRIKLER! " + store_name + "Promosyon Kazandiniz.")
elif store_gelir == limit:
    print("Uyari! " + store_name +" " + str(
        store_gelir) + ": Cok dusuk")                                   # int'a cevirdigimiz geliri print icerisinde str olarak yazdık.
else:
    print(store_name + " Incelemeye devam!")


# Mini Uygulama

# "if", "for" ve Fonksiyonlarının birlikte kullanimi;

salary4 = [1000, 2000, 3000, 4000, 5000]

# Maasi 3000'den az olanlara %20, 3000'den fazla olanlara %10 zam yapmak istiyoruz;

# Iki durum icin iki tane fonksiyon olusturuyoruz;
def maas_ust(x):
    print(x * 10 / 100 + x)


def maas_alt(x):
    print(x * 20 / 100 + x)

# Karar kontrol yapisi olusturuyoruz; (">=" "buyuk ya da esit" demek.)
for i in salary4:
    if i >= 3000:
        maas_ust(i)
    else:                                # Geride kalan durumlar icin.
        maas_alt(i)