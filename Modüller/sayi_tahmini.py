import random
import time

print("""
Sayi Tahmin Oyunu
1 ile 40 arasında sayı tahmin edin.

""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:

    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha yuksek bir sayi söyleyin....")
        tahmin_hakki -= 1
    elif(tahmin > rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayi söyleyin....")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! ",rastgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Tahmin hakikiniz bitti")
        print("Sayimiz",rastgele_sayi)
        break
