## #NESNE YONELIMLI PROGRAMLAMA

# Siniflar ;
# Benzer ozellikler, ortak amac tasiyan, icerisinde metodlar ve degiskenler olan yapilardir.
# Islemlerimizi kolaylastirmak icin olusturdugumuz yapilar.

class Veri_Bilimci():
    bolum = ""                                  # Sinif ozelliklerini tanimliyoruz.
    sql = "EVET"
    deneyim = 0
    bildiği_diller = []


# Siniflarin ozelliklerine erismek;
Veri_Bilimci.bildiği_diller
Veri_Bilimci.bolum
Veri_Bilimci.deneyim

# Siniflarin ozelliklerini degistirmek;
Veri_Bilimci.deneyim = 3
print(Veri_Bilimci.deneyim)


## SINIF ORNEKLENDIRMESI
# Genel sinif ozelliklerini barindiran alt birimler olusturma islemine "Sinif Orneklendirmesi" denir.

class Veri_Bilimci():
    bolum = ""                                  # Sinif ozelliklerini tanimliyoruz.
    sql = "EVET"
    deneyim = 0
    bildigi_diller = []


ali = Veri_Bilimci()                            # Veri_Bilimci sinifinin ozelliklerini barindiran bir alt birim olusturduk.

print(ali.sql)
print(ali.deneyim)

# Ali'nin ozellliklerini degistirmek istiyoruz, "append";
ali.bildigi_diller.append("python")
print(ali.bildigi_diller)

veli = Veri_Bilimci()
veli.bildigi_diller                             # Ali'de yaptigim degisiklik butun sinifi etkiledi. Bunu engellemek icin;


# Ornek Ozellikleri;
class veribilimci():
    bildiği_diller = ["R", "pyhton"]            # Genel yetenek seti belirledik.

    def __init__(self):
        self.bildiği_diller = []                # Her bir ornegin kendi icerisinde degisen ozelliklerden olusabilecegi bilgisini verdik.


ali = veribilimci()
print(ali.bildiği_diller)

veli = veribilimci()
print(veli.bildiği_diller)

ali.bildiği_diller.append("pyhton")             # Ali'nin bildigi dilleri kendi icerisinde degistirdik.
veli.bildiği_diller.append("R")                 # Veli'nin bildigi dilleri kendi icerisinde degistirdik.
print(ali.bildiği_diller)
print(veli.bildiği_diller)

veribilimci.bildiği_diller                      # Genel yetenek seti ciktisini verdi.


# Ayni ornegi sinifa genel yetenek seti olusturmadan yaparsak;
class veribilimci():

    def __init__(self):
        self.bildiği_diller = []                # Her bir ornegin kendi icerisinde degisen ozelliklerden olusabilecesi bilgisini verdik.


ali = veribilimci()
print(ali.bildiği_diller)

veli = veribilimci()
print(veli.bildiği_diller)

ali.bildiği_diller.append("pyhton")             # Ali'nin bildigi dilleri kendi icerisinde degistirdik.
veli.bildiği_diller.append("R")                 # Veli'nin bildigi dilleri kendi icerisinde degistirdik.
print(ali.bildiği_diller)
print(veli.bildiği_diller)

veribilimci.bildiği_diller                      # Genel yetenek seti olusturmadigimiz için, "AttributeError" verdi (attribute = ozellik).


# Ornek Metodları (Ornekler uzerinde calisan fonksiyonlar)

# Uzun yoldan birimlere özellik tanimlamak yerine sinifa fonksiyon tanimliyoruz;
class veribilimci():

    def __init__(self):
        self.bildiği_diller = []
        self.bolum = ""                         # Orneklerin birimden birime göre degisecek ozelliklerini belirledik.

    def dil_ekle(self, yeni_dil):               # yeni_dil: Fonksiyonun argümanı(x), self: Ornekleri baglamak için kullanilir.
        self.bildiği_diller.append(yeni_dil)    # Fonksiyonu tanimladik.


ali = veribilimci()
veli = veribilimci()

ali.dil_ekle("R")
veli.dil_ekle("pyhton")

print(ali.bildiği_diller)
print(veli.bildiği_diller)


## MİRAS YAPILARI

# Daha onceki class ozelliklerini baska bir classda kullanmak;
class employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""                       # Sabit degerlerle tanimladik.


class data_science(employees):                  # Parantez icerisinde ozelliklerini kullanmak istedigimiz sinifin adini yazdik.
    def __init__(self):
        self.Programming = ""


DS = data_science()

# DS. yaptigimizda artik employess sinifinin ozelliklerinin data.science'a eklendigini gorecegiz. (*)


# Fonksiyonel Yapida Sinifi Tanimlamak icin;
class employe_yeni():

    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = employe_yeni("a", "b", "c")

print(ali.Address)
print(ali.FirstName)

