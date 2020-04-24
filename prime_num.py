# Задача 2: "Наибольший простой делитель"
# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?


import math


def biggest_divider(num: int):
    '''
    Function to find the biggest divider of a simple value
    '''
    max_num = 0

    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            max_num = i
            num = num / i

    return max_num


# Test
# number = 13195
# print(biggest_divider(number))

number = 600851475143
print(biggest_divider(number))
