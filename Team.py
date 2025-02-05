n = int(input())
sol = 0
a = [None]*n
for i in range(n):
    a[i] = input()

for j in range(n):
    b,c,d = a[j].split()
    if b == "1":
        if c == "1":
            sol = sol + 1
        else:
            if d == "1":
                sol = sol + 1
            else:
                sol = sol
    else:
        if c == "1":
            if d == "1":
                sol = sol + 1
            else:
                sol = sol
        else:
            sol = sol
print(sol)
