# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Введите количество журавликов: "))
Piter = 0
Sergey = 0
Kate = 0

if Piter == Sergey and Kate == (Piter+Sergey) * 2:
   Piter  = int ((s / 3) / 2)
   Sergey = Piter
   Kate = (Piter+Sergey) * 2
print(Piter, Sergey, Kate)

