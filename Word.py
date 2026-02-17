s = input()
up = 0
low = 0
n = len(s)
for i in range(n):
    if s[i].islower():
        low = low + 1
    else:
        up = up + 1
if up > low:
    print(s.upper())
else:
    print(s.lower())
