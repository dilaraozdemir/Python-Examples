print("""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
""")


işlem = input("Üçgenin için 1 dörtgen için 2: ")

if işlem == "1":
    a = int(input("İlk kenar:"))
    b = int(input("İkinci kenar:"))
    c = int(input("Üçüncü kenar:"))
    if ( a == b and b == c):
        print("Eşkenar Üçgen")
    elif ( a == b or b == c or c == a):
        print("İkizkenar")
    else:
        print("Çeşitkenar")
elif işlem == "2":
    a = int(input("İlk kenar:"))
    b = int(input("İkinci kenar:"))
    c = int(input("Üçüncü kenar:"))
    d = int(input("Dördüncü kenar:"))
    if ((a == c and b == d and a != d) or (a == b and c == d and a != d) or (a == d and c == b and a != b)):
        print("Dikdörtgen")
    elif (a == b and b == c and c == d):
        print("Kare")
    else:
        print("Sıradan dörtgen")

"""Hazır

şekil =  input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

if (şekil == "Dörtgen"):
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))
    
    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
        
    
    
elif (şekil == "Üçgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")
        
else:
    print("Geçersiz Şekil...")

"""