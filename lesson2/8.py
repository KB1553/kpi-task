'''Замінити всі елементи масиву, менші за середнє арифметичне, на 0.'''
arr = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

average = sum(arr) / len(arr)
arr_modified = [x if x >= average else 0 for x in arr]

print("Масив після заміни елементів менших за середнє на 0:", arr_modified)
