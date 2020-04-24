def fibonacci() -> int:
    '''
    Fibbonachi generator
    '''
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def sum_all_fibbonachi_even_numbers(limit: int) -> int:
    '''
    Returns sum of all even fibbonachi numbers which is not greater than limit
    '''
    sum = 0
    for f in fibonacci():
        if f <= limit:
            if (f % 2) == 0:
                sum += f
        else:
            return sum


if __name__ == "__main__":
    print(sum_all_fibbonachi_even_numbers(4000000))
