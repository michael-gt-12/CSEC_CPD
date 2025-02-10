n = int(input())
order = input()
order = list(order.split())
int_order = []
for i in range(n):
    int_order.append(int(order[i]))
police = 0
untreated = 0
for i in range(n):
    if int_order[i] == -1:
        if police > 0:
            police = police - 1
        else:
            untreated = untreated + 1
    else:
        police = police + int_order[i]
print(untreated)
