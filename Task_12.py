# Задача 12
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9


def create_file(path, sep=','):

    berries = [25, 40, 36, 28, 31, 22, 48, 52, 15, 38]
    data = open(path, 'w')
    for i in range(len(berries)):
        data.write(str(berries[i])+sep)
    data.close()
create_file('file_shrub.txt', sep='*')

def read_file(path, sep = '*'):
    f = open(path, "r")
    line = f.readline()
    line = line.split(sep)[:-1]
    line = list(map(int, line))

    f.close()
    return (line)

datas = read_file('file_shrub.txt')

print(read_file('file_shrub.txt'))

def choose_max_pos(berries):
    sum_list =[]
    for i in range(len(berries)-1):
        sum = berries[i]+berries[i+1]+berries[i-1]
        sum_list.append(sum)

    return (max(sum_list), sum_list.index(max(sum_list)))

print(f'Максимальное число ягод и с позиции какого куста: {choose_max_pos(datas)}')