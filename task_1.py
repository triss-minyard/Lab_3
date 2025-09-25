a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
if a<=c and b<=d:
    print("Может")
elif a<=d and b<=c:
    print("Может")
else:
    print("Не может")
