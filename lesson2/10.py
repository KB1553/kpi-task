'''Знайти добуток всіх непарних елементів масиву.'''
arr = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

product = 1
has_odd = False

for x in arr:
    if x % 2 != 0:
        product *= x
        has_odd = True

if has_odd:
    print("Добуток всіх непарних елементів:", product)
else:
    print("Немає непарних елементів для добутку")