numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
positive_n = []
for num in numbers:
    if num > 0:
        positive_n.append(num)
print("Список додатних чисел:", positive_n)