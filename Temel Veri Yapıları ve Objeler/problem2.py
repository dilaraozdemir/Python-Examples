"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

boy = int(input("boy: "))
kilo = int(input("kilo: "))

print("İndeks : {}".format(kilo/boy))