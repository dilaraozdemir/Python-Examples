print("""
Atm Makinesine hosgeldiniz
İşmler;
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme
Programdan çıkmak için 'q'ya basın
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz: ")

    if(işlem == "q"):
        print("Yine bekleriz")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktari giriniz:"))
        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Miktari giriniz:"))
        if(bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz...")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz işlem")
