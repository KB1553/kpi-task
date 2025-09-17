a=input("Введіть число: ")

suma=0
for b in a:
    if b.isdigit():  
        suma+=int(b)

print("Сума цифр числа:", suma)