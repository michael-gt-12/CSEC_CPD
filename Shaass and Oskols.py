n = int(input())
birds = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    wire, bird = map(int, input().split())
    wire -= 1
    left_birds = bird - 1
    right_birds = birds[wire] - bird
    if wire > 0:
        birds[wire - 1] += left_birds
    if wire < n - 1:
        birds[wire + 1] += right_birds
    birds[wire] = 0
for count in birds:
    print(count)
