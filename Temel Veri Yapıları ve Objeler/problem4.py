"""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""

ad = input("Oyuncunun adi: ")
soyad = input("Oyuncunun soyadi: ")
numara = int(input("Oyuncunun numara: "))

bilgiler = [ad,soyad,numara]



print("Oyuncunun Adı: {}\nOyuncunun Soyadı: {}\nOyuncunun numara: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

