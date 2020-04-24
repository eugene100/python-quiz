# Задача 7: "Самая длинная последовательность Коллатца"

# Следующая повторяющаяся последовательность определена для множества
# натуральных чисел:
# n → n/2 (n - четное)
# n → 3n + 1 (n - нечетное)
# Используя описанное выше правило и начиная с 13, сгенерируется следующая
# последовательность:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит
# 10 элементов. Хотя это до сих пор и не доказано
# (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким
# образом последовательности оканчиваются на 1.
# Какой начальный элемент меньше миллиона генерирует самую длинную
# последовательность?

# Примечание: Следующие за первым элементы последовательности могут быть
# больше миллиона.


class Collatz():

    def __init__(self, max_num: int):
        self.max_num = max_num

        self.num_seq = dict()

        # Maximum number should be odd
        if (self.max_num % 2) == 0:
            self.max_num -= 1

        self.loop()
        self.seq = max(self.num_seq.values())
        self.max_num = [k for k, v in self.num_seq.items() if v == self.seq]

    def loop(self):
        for n in range(self.max_num, 1, -2):
            z = self.seq(n)
            self.num_seq.update(z)

    def seq(self, num: int):
        n = num
        cur_seq = dict()
        seq = 1
        while n != 1:
            cur_seq[n] = seq
            if n in self.num_seq:
                return self.reverse_seq(cur_seq, self.num_seq[n] + seq)
            if (n % 2) == 0:
                n = self.even(n)
            else:
                n = self.odd(n)
            seq += 1
        return self.reverse_seq(cur_seq, seq+1)

    def even(self, num: int):
        return num//2

    def odd(self, num: int):
        return 3*num+1

    def reverse_seq(self, seq: dict, max_num):
        for k, v in seq.items():
            seq[k] = max_num - v
        return seq


collatz = Collatz(1000000)
print(f'Number: {collatz.max_num} Sequences: {collatz.seq}')
