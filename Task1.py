# Найти сумму элементов одномерного массива. Размер произвольный.
#    Элементы листа вводятся с клавиатуры.

numbers = []
p = 0
i = 0
while True:
    x = int(input())
    numbers.append(x)
    p += x
    i += 1
    if i > 5:
        break
print(numbers)
print(f"Сумма элементов списка: {p}")

