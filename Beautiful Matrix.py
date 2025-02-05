count = 0
a = [None]*5
for i in range(5):
    b = "".join(input().split())
    a[i] = b
for i in range(5):
    for j in range(5):
        if a[i][j] == "1":
            row = i+1
            col = j+1
while row < 3 or row > 3:
    if row < 3:
        row = row + 1
        count = count + 1
    elif row > 3:
        row = row - 1
        count = count + 1
    

while col < 3 or col > 3:
    if col < 3:
        col = col + 1
        count = count + 1
    elif col > 3:
        col = col - 1
        count = count + 1
    
print(count)
