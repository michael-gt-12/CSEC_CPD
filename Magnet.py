n = int(input())
s = []
group = 0
for i in range(n):
    s.append(input())
for i in range(n-1):
    if s[i][1] != s[i+1][0]:
        group = group
    else:
        group = group + 1
group = group + 1
print(group)
