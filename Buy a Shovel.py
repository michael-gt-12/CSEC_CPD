price,r = list(map(int,input().split()))
shovel = 1
k = price
while True:
    if k % 10 == 0 or k % 10 == r:
        print(shovel)
        break
    else:
        shovel = shovel + 1
        k = k + price
