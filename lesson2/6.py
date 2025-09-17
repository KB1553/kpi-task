arr = []
print("Введіть 20 елементів:")  # Окремий рядок для повідомлення

for i in range(20):
    x = int(input(f"Елемент {i + 1}: "))
    arr.append(x)

print("Масив:", arr)