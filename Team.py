n = int(input())
views = []
for _ in range(n):
    views.append(list(map(int,input().split())))
count = 0
for question in views:
    if question.count(1) >= 2:
        count += 1
print(count)
