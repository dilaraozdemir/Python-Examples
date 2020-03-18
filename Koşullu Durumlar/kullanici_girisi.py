
sys_kullanici_adi = "Dilara"
sys_parola = "12345"

kullanici_adi = input("Kullanici Adi: ")
parola = input("Parola: ")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Parola hatali..")
elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Ad hatali..")
elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Ad ve parola hatali..")
else:
    print("Sisteme basarıyla giris yaptiniz..")