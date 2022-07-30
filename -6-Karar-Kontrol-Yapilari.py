### KARAR - KONTROL YAPILARI

# 1) True / False uygulamalari;
limit = 500
print(limit == 500)
print(limit == 600)


# 2) "if" ;
limit = 5000
salary = 4000

if salary < limit:                          # if, bu kosul true saslandiginda devam eder.
    print("Gelir, limitten kucuk")

if salary > limit:                          # if, false durumunda calısmaya devam etmez.
    print("Gelir, limitten buyuk.")


# 3) "else" ;
limit = 50000
salary = 30000

if salary > limit:
    print("Salary, sinirden kucuk")

if salary == limit:
    print("salary, limite esit degil.")


# "elif" ("Birden fazla kosul" kullanmak icn kullanilir.)
limit = 50000
salary1 = 70000
salary2 = 25000
salary3 = 50000

if salary1 > limit:                         # True oldugu igin if calisti, gerisini okumadi.
    print("Tebrikler, hediye kazandiniz.")

elif salary1 < limit:
    print("Uyari!")

else:                                       # "else" en son yazilir, geride kalan kosul icin kullanilir.
    print("Takibe devam.")

limit = 50000
salary1 = 70000
salary2 = 25000
salary3 = 50000

if salary2 > limit:                         # False oldugu için "if" calismadi.
    print("Tebrikler, hediye kazandiniz.")

elif salary2 < limit:                       # False oldugu icin "else" calisti, gerisini okumadi.
    print("Uyari!")

else:                                       # "else" en son yazilir, geride kalan kosul icin kullanilir.
    print("Takibe devam.")

limit = 50000
salary1 = 70000
salary2 = 25000
salary3 = 50000

if salary3 > limit:                         # False oldugu icin "if" calismadi.
    print("Tebrikler, hediye kazandınız.")

elif salary3 < limit:
    print("Uyari!")

else:                                       # "else" en son yazilir, geride kalan kosul icin kullanilir.
    print("Takibe devam.")

# Donguler, iteratif islemleri yerine getirmek icin kullandigimiz yapilardir.
# Nesnelerdeki elemanlara tek tek erişme


# "for" döngüsü;
students = ["anıl", "rumeysa", "tilda", "defne"]
for i in students:
    print(i)                                # i;  bir temsili degiskendir.

salary = [1000, 2000, 3000, 4000]
for a in salary:
    print(a)


# Döngü ve Fonksiyonların Birlikte Kullanilmasi;
def kare_al(x):
    print(x ** 2)


kare_al(2)                                  # Veriler cok oldugunda bunu kullanmamak icin;

salary = [1000, 2000, 3000, 4000]
for i in salary:
    print(i)


# Maaşlara %20 zam yapmak istiyoruz;
print(salary[0] * 20 / 100 + salary[0])     # Her ifade icin tek tek indexe gidip ugrasmak istemiyoruz;

salary = [1000, 2000, 3000, 4000]


def zam_yap(x):                             # Fonksiyonu tanimliyoruz.
    print(x * 20 / 100 + x)


for i in salary:                            # Donguyu devreye sokuyoruz.
    zam_yap(i)


# "break" ve "continue" ;

# "break"; Donguler icerisinde belirli sartı saglayan ifadeler yakalandıgında donguyy bitirmek icin kullanilir.

salary5 = [7500, 1750, 3000, 8652, 3025, 5000]

# Döngüyü 3000de birakmak istiyoruz;
salary5.sort()                              # "sort" ile listeyi siraladik.

for i in salary5:
    if i == 3000:
        break
    print("Kesildi")
    print(i)                                # Kesilmeden onceki degerleri de gormek istedigim icin.

salary5 = [7500, 1750, 3000, 8652, 3025, 5000]
salary5.sort()

for i in salary5:
    if i == 3000:
        continue                            # 3000'i atlayarak devam ettik.
    print(i)


# "while" (Bu sart saglandiginda);
number = 1

while number < 10:
    number += 1                             # "+=" üzerine 1 ekleyerek yeni deger atadik.
    print(number)