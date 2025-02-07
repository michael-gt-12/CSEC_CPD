s = input()
low_case = "abcdefghijklmnopqrstuvwxyz"
up = 0
low = 0
n = len(s)
for i in range(n):
    if s[i] in low_case:
        low = low + 1
    else:
        up = up + 1
if up > low:
    print(s.upper())
else:
    print(s.lower())
