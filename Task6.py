# 6) Массив А вводится с клавиатуры. Сформировать новый массив В,
#    состоящий из четных элементов массива А. Элементы вводятся с клавиатуры.
#    Размер n.
import random
n = int(input('enter length: '))
A = []
B = []
i = 0
while i < n:
    A.append(random.randrange(100))
    if A[i] % 2 == 0:
        B.append(A[i])
    i += 1
print(A, "\n", B)

