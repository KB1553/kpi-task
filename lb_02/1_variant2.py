N = int(input("Введіть число N: "))

for i in range(10, N + 1):
    digits = [int(d) for d in str(i)]
    if 0 not in digits and all(i % d == 0 for d in digits):
        print(i)