print("""
Faktöriyel Bulma
Çıkmak için 'q'ya basiniz
""")
while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
        print("faktoriyel",faktoriyel)