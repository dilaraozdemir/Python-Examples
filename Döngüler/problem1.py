print("""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
""")

sayi = int(input("Enter a number to check perfect or not "))
total = 0
i = 1
while (i < sayi):
    if(sayi % i == 0):
        total += i
    i += 1

if (sayi == total):
    print("Perfect")
else:
    print("Not perfect")