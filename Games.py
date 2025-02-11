n = int(input())
kit = []
for i in range(n):
    kit.append(list(map(int,input().split())))
guest_kit = 0
for i in range(n):
    host_team = kit[i]
    for j in range(n):
        if j != i:
            if host_team[0] == kit[j][1]:
                guest_kit += 1
print(guest_kit)
