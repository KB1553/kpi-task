N = int(input("Кількість поїздок (N): "))
k = int(input("Кількість квитків у пачці (k): "))
p1 = int(input("Ціна одного квитка (p1): "))
p2 = int(input("Ціна пачки квитків (p2): "))

cost1 = N * p1

cost2 = ((N + k - 1) // k) * p2  

packs = N // k
single = N % k
cost3 = packs * p2 + single * p1

print("Мінімальні витрати:", min(cost1, cost2, cost3))