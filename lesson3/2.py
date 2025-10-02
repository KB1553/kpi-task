lst = list(map(int, input("Введіть числа через пробіл: ").split()))
count = sum(1 for x in lst if x % 3 == 0)
print("Кількість чисел, що діляться на 3:", count)