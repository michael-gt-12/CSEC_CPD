n = int(input())
cubes = input()
cub_lis = list(map(int , cubes.split()))
cub_lis.sort()
for i in range(n):
    print(cub_lis[i] , end = " ")
