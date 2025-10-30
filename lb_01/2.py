x, y = map(float, input("Введіть координати точки (x y): ").split())

if x > 0 and y > 0:
    print("1 чверть")
elif x < 0 and y > 0:
    print("2 чверть")
elif x < 0 and y < 0:
    print("3 чверть")
elif x > 0 and y < 0:
    print("4 чверть")
elif x == 0 and y == 0:
    print("Точка в початку координат")
elif x == 0:
    print("Точка на осі Y")
else:
    print("Точка на осі X")