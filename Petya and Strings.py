str1 = input().upper()
str2 = input().upper()
n = len(str1)
count = 0

for i in range(n):
    if str1[i] == str2[i]:
        count = 0
    else:
        if str1[i] < str2[i]:
            count = -1
            break
        elif str2[i] < str1[i]:
            count = 1
            break
print(count)
