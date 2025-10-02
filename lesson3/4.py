lst = list(map(int, input("Введіть числа через пробіл: ").split()))
lst = [-1 if x % 5 == 0 else x for x in lst]
print("Оновлений список:", lst)
