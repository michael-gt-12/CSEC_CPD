num= input()
n,h = num.split()
n,h = int(n),int(h)
w = 0
a = list(map(int , input().split()))
for i in range(n):
    if a[i]<=h:
        w = w + 1
    else:
        w = w + 2
print(w)
