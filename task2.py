grades = list(map(int,input("введите щценки: ").split()))
if grades.count(2) > 0:
    print("Отчислен")
else:
    print("Учится")
print(grades)
