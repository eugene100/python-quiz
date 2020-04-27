def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def sum_digits(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res


if __name__ == "__main__":
    print(sum_digits(factorial(100)))
