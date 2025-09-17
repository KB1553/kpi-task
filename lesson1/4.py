a=int(input("число:"))
b=1
print("Таблиця множення для:", a)

for i in range (1, 11):
    print(a, "*", b, "=", a * i)
    b+=1