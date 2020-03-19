import math


def hesapmakinesi(sayi,secim):
    if(secim == "cos"):
        return math.cos(sayi)
    elif(secim == "sin"):
        return math.sin(sayi)
    elif (secim == "pow"):
        return math.pow(sayi,sayi)
    elif (secim == "factorial"):
        return math.factorial(sayi)
    elif (secim == "floor"):
        return math.floor(sayi)
    else:
        print("yanlis secim")

sayi = input("Birinci sayiyi giriniz:")
sayi = int(sayi)
secim = input("Seciminizi giriniz: ")
print(hesapmakinesi(sayi,secim))