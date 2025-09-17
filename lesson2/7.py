'''Знайти мінімальний непарний елемент масиву.'''
arr = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

odd_elements = [x for x in arr if x % 2 != 0]

if odd_elements:
    print("Мінімальний непарний елемент:", min(odd_elements))
else:
    print("Немає непарних елементів")