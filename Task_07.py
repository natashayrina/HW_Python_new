# Задача 7:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8
#
n = int(input("Введите число N = "))

arr = []
num = 2
for i in range(n-1):
    if num ** i <= n:
        arr.append(num ** i)

    else:
        i = n
print(arr)
