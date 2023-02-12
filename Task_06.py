# Задача 6:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2

from random import randint
number_1 = randint(0, 1001)
number_2 = randint(0, 1001)

sum_of_numbers = number_1 + number_2
mult_of_numbers = number_1 * number_2

mult_of_numbers = (sum_of_numbers - number_2) * number_2
mult_of_numbers = sum_of_numbers * number_2 - number_2 ** 2
number_2 ** 2 - sum_of_numbers * number_2 + mult_of_numbers
d = sum_of_numbers **2 - 4 * mult_of_numbers
number_2 = int(sum_of_numbers / 2 + d**(0.5)/2)
number_1 = int(sum_of_numbers / 2 - d ** (0.5)/2)

print(f'Cумма чисел = {sum_of_numbers}')
print(f'Произведение чисел = {mult_of_numbers}')
print((f'Загаданные числв это: {number_1} и {number_2}.'))