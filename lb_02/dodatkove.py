from itertools import product

nums = range(1, 15)

for a, b, d, e, f, g, h, i in product(nums, repeat=8):  

    row1 = a + b - 9
    row2 = d - e * f
    row3 = g + h - i

    col1 = a + d + g
    col2 = b - e + h
    col3 = 9 - f - i  

    if row1 == row2 == row3 == col1 == col2 == col3 == 4:
        print("Розв’язок знайдено:")
        print(f"{a}   {b}   9")
        print(f"{d}   {e}   {f}")
        print(f"{g}   {h}   {i}")
        break
else:
    print("Розв’язків не знайдено")
