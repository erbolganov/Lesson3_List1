# Найти сумму элементов массива с четными номерами, содержащего N элементов.
# Элементы вводятся с клавиатуры.

numbers = []
p = 0
s = 0
i = 0
n = int(input("Вводите размер массива: "))
while True:
    x = int(input())
    numbers.append(x)
    if i % 2 == 0:
        p += x
    if x % 2 == 0:
        s += x
    i += 1

    if i == n:
        break
print(numbers)
print(f"Сумма элементов четными номерами : {p}")
print(f'Сумма четных элементов: {s}')