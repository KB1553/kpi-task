numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
count = 0
for num in numbers:
    if num < 0:
        count += 1

print("Кількість від’ємних чисел:", count)