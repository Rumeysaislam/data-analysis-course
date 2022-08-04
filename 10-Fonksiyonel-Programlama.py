### FONKSIYONEL PROGRAMLAMA

import numpy as np  # numpy isimli kutuphanemi np kisaltmasi yaparak calisma dizinime ekledik.

a = np.array([1, 2, 3, 4])  # np.array yaparak diziyi numpy'in taniyacagi sekle cevirdik.
b = np.array([2, 3, 4, 5])

print(a * b)

## Vektorel Islem Yapmamizi Saglayan Fonksiyonlar

liste = [1, 2, 3, 4]  # Listenin her bir elemanina 10 eklemek istiyoruz;

for i in liste:
    print(i + 10)

# "map" ile yazacak olursak; map: verilen bir nesnenin uzerinde tanimlanacak fonksiyonu calistirma imkani verir.

liste = [1, 2, 3, 4]

list(map(lambda x: x + 10, liste))

# "filter"; kosul arar, saglayanlari filtreler.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0,
            liste))  # "x % 2 == 0" ikiye bolumunden kalan sifir demek. True donenleri listede gosterir.

# "reduce"; Indirgeme islemi yapar;

from functools import reduce  # Kutuphane icerisinden "reduce" fonksiyonunu aldik.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reduce(lambda a, b: a + b, liste)  # Tum sayilar toplandi.
