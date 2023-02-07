# 5)  В заданном одномерном  массиве, состоящем из n  целых чисел,
#                   подсчитать количество четных элементов.
import random
n = int(input('Enter length: '))
num = []
i = 0
q = 0
while i < n:
    num.append(random.randrange(100))
    if num[i] % 2 == 0:
        q += 1
    i += 1
print(num)
print('количество четных элементов: ', q)

