"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = int(input("a: "))
b = int(input("b: "))

print("Old a: {}\nOld b: {}\n".format(a,b))

temp = a
a = b
b = temp

print("New a: {}\nNew b: {}\n".format(a,b))
