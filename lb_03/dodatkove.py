def is_lucky(ticket):
    s = f"{ticket:06d}"
    return sum(map(int, s[:3])) == sum(map(int, s[3:]))

def count_lucky(a1, a2):
    count = 0
    for i in range(a1, a2 + 1):
        if is_lucky(i):
            count += 1
    return count

a1 = int(input("Введіть a1: "))
a2 = int(input("Введіть a2: "))
print("Кількість щасливих квитків:", count_lucky(a1, a2))