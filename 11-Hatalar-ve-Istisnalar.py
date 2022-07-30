### HATALAR ve ISTISNALAR (Exceptions)

# ZeroDivisionError (Sifir Bolme Hatasi);
a = 10
b = 0 a/ b

# try-except yapisi;
try:  # Dene, kodu calistirmaya calis.
    print(a / b)

except ZeroDivisionError:  # Boyle bir hata olursa, istisna olarak çalıştır.
    print("Payda da sıfır olmaz")  # Bilgi notu eklemek de olurdu.


# TypeError;
a = 10
b = "2"

try:
    print(a / b)

except TypeError:
    print("int ve str problemi")