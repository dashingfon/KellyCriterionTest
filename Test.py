from random import randint

ROUNDS = 100
YAY = 0
NAY = 0
PERCENT = 60

for i in range(ROUNDS):
    num = randint(1,100)
    if num > PERCENT:
        NAY += 1
    else:
        YAY += 1

print(f'numbers below {PERCENT} appeared {NAY/ROUNDS*100} percents')
print(f'numbers above {PERCENT} appeared {YAY/ROUNDS*100} percents')


