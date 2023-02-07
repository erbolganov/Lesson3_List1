# Найти наименьший элемент одномерного массива, состоящего из n элементов.
# Элементы вводятся с клавиатуры.
numbers = []
i = 0
n = int(input("Вводите размер массива: "))
while True:
    x = int(input())
    numbers.append(x)
    i += 1
    if i == n:
        break

print(numbers)
print("наименьший элемент: ", min(numbers))