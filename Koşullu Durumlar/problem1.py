
print("""
****************
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
****************
""")

boy = int(input("boy: "))
kilo = int(input("kilo: "))

indeks = kilo/boy*boy

if (indeks<18.5):
    print("Zayif")
elif (indeks>=18.5 and indeks>25):
    print("Normal")
elif (indeks>=25 and indeks>=30):
    print("Normal")
elif (indeks>30):
    print("Normal")

