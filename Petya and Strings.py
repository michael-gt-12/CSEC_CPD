str1 = input()
str2 = input()
n = len(str1)
count = 0
strr1 = []
strr2 = []
for i in range(n):
    strr1.append(str1[i].capitalize())
    strr2.append(str2[i].capitalize())

for i in range(n):
    if strr1[i] == strr2[i]:
        count = 0
    else:
        if strr1[i] < strr2[i]:
            count = -1
            break
        elif strr2[i] < strr1[i]:
            count = 1
            break
print(count)
