width = int(input("Ширина: "))
height = int(input("Висота: "))
border = input("Символ контуру: ")
fill = input("Символ заповнення: ")

for i in range(height):
    for j in range(width):
        if i == 0 or i == height-1 or j == 0 or j == width-1:
            print(border, end="")
        else:
            print(fill, end="")
    print()