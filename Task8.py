# 8) Создайте массив из 15 целочисленных элементов
#    и определите среди них минимальное значение.
import random

n = 15
a = []
for i in range(n):
    x = random.randrange(50)
    a.append(x)

print(a)
print('минимальное значение: ', min(a))