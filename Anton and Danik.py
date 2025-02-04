n = int(input())
s = input()
s = list(s)
A = 0
D = 0
for i in range(n):
    if s[i]=="A":
        A = A+1
    else:
        D = D+1
if A > D:
    print("Anton")
elif A < D:
    print("Danik")
else:
    print("Friendship")

