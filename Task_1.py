# 1)Есть список. Найти количество трехзначных чисел в нем.

# my_list = [12, 123, 258, 23, 89, 1254, 639, 54, 6, 256, 47, 458, 389]
# index = 0
# for num in my_list:
#     if 99 < num < 1000:
#         index +=1
# print (index)

import random
n = int(input("Введите длину списка: "))
my_list = []
index = 0
for i in range(n):
    my_list.append(random.randint(1, 1999))
print (my_list)
for num in my_list:
    if 99 < num < 1000:
        index += 1
print(index)



