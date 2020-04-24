# Задача 6: "Сложение простых чисел"
# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.


def primes():
    '''
    Generator returns next prime number
    '''
    primes = [2]
    n = 3
    yield 2
    while True:
        is_prime = True
        for p in primes:
            if (n % p) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 2


def sum_prime(max_num: int):
    sum = 0
    for p in primes():
        if not (p < max_num):
            break
        sum += p
    return sum


print(sum_prime(2000000))
