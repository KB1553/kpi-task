numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
print("Сума квадратів чисел:", sum(num**2 for num in numbers))