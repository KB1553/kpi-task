import math

def circle_area(r):
    return math.pi * r**2

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

def main():
    print("1 – Коло, 2 – Прямокутник, 3 – Трикутник")
    choice = int(input("Виберіть фігуру: "))

    if choice == 1:
        r = float(input("Введіть радіус: "))
        print("Площа круга =", circle_area(r))
    elif choice == 2:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        print("Площа прямокутника =", rectangle_area(a, b))
    elif choice == 3:
        a = float(input("Введіть основу: "))
        h = float(input("Введіть висоту: "))
        print("Площа трикутника =", triangle_area(a, h))
    else:
        print("Невірний вибір!")

main()