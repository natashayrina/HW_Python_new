# Задача 13
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def raise_in_degree(a, b):
    if a in [0, 1] and b in [1, 2]:
        return 1
    return a**b

a = int(input("Введите число a = "))
b = int(input("Введите число b= "))
print(raise_in_degree(a, b))
