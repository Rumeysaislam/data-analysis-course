# int:integer/ str:string, float, complex
type(9.2)
type(3 + 2 * 1j)
type("kelime")
type(3)
type("3")                                                # Tirnak içerisine yazilan sayi da olsa str olarak cikar !


# complex sayi yazmak;
type(5 + 2 * 1j)
type(3 + 8 * 1j)
type(5 + 6 * 2j)


# Tip donusumleri;
int(12.3)  # Float iken int olarak cikti
float(15)  # int iken float cikti
complex(13)  # int iken complex cikti
str(16)  # String olarak cikti; '16'


# Kod ciktisini ekrana yazdirmak;
print(type(12.6))
print(type(int(12.6)))
print(type(str(12.6)))


# "sep" ile fonk. icinde betimleme yapmak;
print("Her", "seyi", "halledecegim.")
print("Her seyi", "halledeceğim.", sep=" ")             # iki kelime arasina " " ekledik.
print("Her", "seyi", "halledecegim.", sep="_")          # iki kelime arasina "-" ekledik.


# stringlerde "+" ve "*" ;
print("Her" + "seyi" + "halledeceğim.")
print("Her" + " seyi" + " halledeceğim.")               # Kelimenin onune bosluk birakarak iki kelime arasina bosluk koydum.
print("Power" * 3)


# integerlarda "+" , "-" , "*" , "/" ;
print(30 * 22)
print(30 / 4)
print(5896 + 6325)
print(985852 - 14586)

a = 55
b = 32
c = a * b
print(a)
print(b)
print(c)
print(c / a)
print(3 ** 2)               # Karesini aldık.
print(3 ** 3)               # Kupunu aldık.