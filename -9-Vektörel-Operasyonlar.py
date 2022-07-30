# VEKTOREL OPERASYONLAR

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# Amacimiz her elemanin indexine gore birbiriyle carpmak;

ab = []                                 # Carpma islemini saklamak adina global alanda bos bir liste tanimliyoruz.

range (0, len(a)) #out: (0,4)
for i in range (0, len(a)):             # a'nin icerisinde sifirdan itibaren kac eleman varsa i gezin demis olduk.
    print (i)
    ab.append(a[i] * b[i])
    print (ab)                          # Nesne yonelimli programlama ozellikleriyle bir döngü yazarak iki vektotu carptık.