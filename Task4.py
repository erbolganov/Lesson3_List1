# 4)  В заданном одномерном  массиве, состоящем из n  целых чисел,
#  подсчитать количество нулей.

import random
massiv = []
i = 0
n = int(input("Enter length of list: "))
while True:
    x = random.randrange(0, 10)
    massiv.append(x)
    i += 1
    if i == n:
        break

print(massiv)
print(massiv.count(0))