### FONKSIYONLAR
## Fonksiyon Okuryazarlıgı: Fonksiyonun dokumantasyonuna ulasmak.

# Fonksiyon Tanimlama "def";
def kare_al(x):
    print(x**2)
kare_al(3)
kare_al(4)
kare_al(25)


# Bilgi Notu ile Cıktı Uretmek;
def kare_al(x):
    print("Girilen Sayının Karesi:" + str(x**2))            # Numerik ifade str olarak yazilir ve ikisinin de str olmasi saglanir.
kare_al(6)
kare_al(56)

def kare_al(x):
    print("Girilen Sayı:" + str(x) + ", Girilen Sayinin Karesi:" + str(x**2))
kare_al(32)


# Iki Argumanli Fonksiyon Tanimlama;
def carpma_yap(x, y):
    print("Çarpım:" + str(x * y))
carpma_yap(65, 12)


# On tanimli fonksiyon yazma; (y'ye başka deger atandiğinda on degeri gozardı eder.)
def carpma_yap(x, y=4):
    print("Çarpım:" + str(x * y))
carpma_yap(98)
carpma_yap(98, 9)

def carpma_yap(x, y):
    print("Çarpım:" + str(x * y))
carpma_yap(y = 65, x = 98)                                  # Bu sekilde siralamadan bagimsiz, argumanlarin isimlerini yazarak da islem yapabiliriyoruz.


# Fonksiyonlar, program dilleri icerisinde tekrar eden gorevleri yerine getirmek
# ve var olan isleri daha pragmatik sekilde gerceklestirmek icin kullanilir.

def ortalama_hesabi(x,y,z):
    print("Alınan Notlar:" + str(x) + str(y) + str(z) + "Ortalama:" + str((x + y + z) / 3))
ortalama_hesabi(35, 65, 85)


# Fonksiyonlarin Ciktisini "Girdi" olarak kullanmak, "return";
def ortalama_hesabi(x,y,z):
    return( (x + y + z) / 3)
ortalama_hesabi(25, 35, 45)
cikti = ortalama_hesabi(25, 35, 45)
ortalama_hesabi(25, 35, 45) * 3

def ortalama_hesabi(x, y, z):
    return( (x + y + z) / 3)
ortalama_hesabi(25, 35, 45)
cikti = ortalama_hesabi(25, 35, 45)
cikti * 3

#Local etki alanindan Global Etki alanina gecmek icin fonksiyon icerisinde global degisken anilir.

x = [3, 2, 5, 6, 8]
print(x)
def eleman_ekle(y):
    print( str(x + y) + " ifade eklendi")
eleman_ekle([9])