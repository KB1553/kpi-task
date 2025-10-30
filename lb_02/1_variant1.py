N = int(input("Введіть число N: "))
found = False

for a in range(int(N ** (1/3)) + 1):
    for b in range(int(N ** (1/3)) + 1):
        if a**3 + b**3 == N:
            print(a, b)
            found = True
            break
    if found:
        break

if not found:
    print("impossible")