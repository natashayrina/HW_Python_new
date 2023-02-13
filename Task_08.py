# Задача 8.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
arr = []
n = int(input("Введите длину массива: "))

for i in range(n):
    arr.append(random.randint(0, 10))
print(arr)

number = int(input("Какое число будем искать? "))
k = 0
trigger = 1
for item in arr:
    if item == number:
        k += 1
        trigger = 0

if trigger ==1:
        print(f'Числа {number} нет в списке')
print(k)
