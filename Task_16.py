# Задача 16:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list = []
n = int(input("Введите длину списка - "))
for i in range(n):
    list.append(random.randint(1, 100))
print (list)

num_1 = int(input("Начало диапазона - "))
num_2 = int(input("Конец диапазона - "))

list_pos = []
for i in range(n):
    if  num_2 > list[i] > num_1:
        list_pos. append(i)
print(*list_pos)