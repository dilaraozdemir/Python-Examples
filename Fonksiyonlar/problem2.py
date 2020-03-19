print("""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
""")

def ebob(s1,s2):
    i = 1
    ebob = 1

    while(i <= s1 and i <= s2):
        if(not(s1 % i) and not (s2 % i)):
            ebob = i
        i += 1
    return ebob
while True:
    s1 = int(input("Sayı-1:"))
    s2 = int(input("Sayı-2:"))

    print("Ebob:", ebob(s1, s2))