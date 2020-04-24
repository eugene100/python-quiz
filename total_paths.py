# Задача 8: "Пути через таблицу"

# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только
# вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?

import math


def total_paths(gridsize: int):
    '''
    Решение с помощью итераций
    '''
    total = 0
    for i in range(1, int('1' + '0'*(gridsize*2-1), 2)):
        if bin(i).count('1') == gridsize:
            total += 1
    return total*2


def math_total_paths(gridsize: int):
    '''
    Матемапически
    '''
    return int(math.factorial(2*gridsize)/(math.factorial(gridsize)**2))


# print(total_paths(13))
print(math_total_paths(20))
