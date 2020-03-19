print("""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
""")


def mukemmel(sayi):
    total = 0
    i = 1
    while (i < sayi):
        if (sayi % i == 0):
            total += i
        i += 1
    return total
while True:
    sayi = int(input("Enter a number to check perfect or not "))

    if (sayi == mukemmel(sayi)):
        print("Perfect")
    else:
        print("Not perfect")