n = int(input())
cub_lis = list(map(int , input().split()))
cub_lis.sort()
for i in range(n):
    print(cub_lis[i] , end = " ")
