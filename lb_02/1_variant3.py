N = int(input("Введіть натуральне число N (100 <= N <= 999999): "))

if N < 100 or N > 999999:
    print("Помилка: N має бути в межах 100...999999.")
else:
    digits = [int(d) for d in str(N)]
    diff = digits[1] - digits[0]
    arif = all(digits[i] - digits[i-1] == diff for i in range(2, len(digits)))
    print("Yes" if arif else "No")