numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
diff = max(numbers) - min(numbers)
print("Різниця між найбільшим та найменшим елементом:", diff)