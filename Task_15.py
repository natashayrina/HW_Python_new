# Задача 15:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import array

a1 = int(input("Введите первый элемент списка -"))
n = int(input("Введите количество элементов в списке - "))
d = int(input("Множитель d = "))

array = [a1 + (i - 1) * d for i in range(1, n + 1)]

print(*array)

