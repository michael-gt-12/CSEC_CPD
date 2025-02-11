s = input()
letters ="abcdefghijklmnopqrstuvwxyz"
n = len(s)
pointer = "a"
count = 0
for i in range(n):
    if s[i] == pointer:
        count = count
    else:
        distance = abs(letters.index(pointer)-letters.index(s[i]))
        if distance <= 13:
            count = count + distance
            pointer = s[i]
        else:
            distance = 26 - distance
            count = count + distance
            pointer = s[i]
print(count)
