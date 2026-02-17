n = int(input())
s = input()
anton = 0
danik = 0
for char in s:
    if char == "A":
        anton += 1
    else:
        danik += 1
if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")

