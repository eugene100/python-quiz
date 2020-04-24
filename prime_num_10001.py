'''
Задача 5: "10001-ое простое число"
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
'''


def prime_num(num: int):
    primes = [2]
    n = 3
    while len(primes) < num:
        is_prime = True
        for p in primes:
            if (n % p) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 2
    return primes[-1]


print(prime_num(10001))
