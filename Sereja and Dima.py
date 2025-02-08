n = int(input())
num = input()
s = list(num.split())
cards = []
for i in range(n):
    cards.append(int(s[i]))
sereja = 0
dima = 0
turn = 1
while turn <= n:
    if turn % 2 != 0:
        if cards[0] >= cards[-1]:
            sereja = sereja + cards[0]
            cards.pop(0)
            turn = turn + 1
        else:
            sereja = sereja + cards[-1]
            cards.pop(-1)
            turn = turn + 1
    else:
        if cards[0] >= cards[-1]:
            dima = dima + cards[0]
            cards.pop(0)
            turn = turn + 1
        else:
            dima = dima + cards[-1]
            cards.pop(-1)
            turn = turn + 1
print(sereja,dima)
