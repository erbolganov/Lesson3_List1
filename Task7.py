# 7) Введите с клавиатуры в массив пять целочисленных значений.
#    Выведите их в одну строку через запятую.
#    Получите для массива среднее арифметическое.

a = input('Enter elements: ').split(',')
q = 0
print(len(a))
for i in range(len(a)):
    q += int(a[i])
print('среднее арифметическое значение массива: ', q / len(a))


