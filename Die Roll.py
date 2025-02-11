from fractions import Fraction
y,w = list(map(int,input().split()))
die = [1,2,3,4,5,6]
dot = []
for i in range(6):
    if die[i] >= y and die[i] >= w:
        dot.append(die[i])
num = len(dot)
den = len(die)
result = Fraction(num, den)
print(f"{result.numerator}/{result.denominator}")
