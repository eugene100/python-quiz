# Задача 9: "Счет букв в числительных"

# Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
# Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
# Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.

ones = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
       ]

tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

ones_len = [len(i) for i in ones]
tens_len = [len(i) for i in tens]
hundred_len = len('hundred')
thousand_len = len('thousand')
and_len = len('and')
# print(ones_len[3])

count_l = 0

for num in range(1, 1001):
    if num < 20:
        count_l += ones_len[num]
    elif num < 100 and num % 10 == 0:
        count_l += tens_len[int(num/10 - 1)]
    elif num < 1000 and num % 100 == 0:
        count_l = count_l + ones_len[int(num/100)] + hundred_len
    elif num == 1000:
        count_l += ones_len[1] + thousand_len
    elif num < 100 and num % 10 != 0:
        count_l = count_l + tens_len[int(num//10 - 1)] + ones_len[int(num % 10)]
    elif num < 1000:
        if num % 100 < 20:
            count_l = count_l + ones_len[int(num//100)] + hundred_len + and_len + ones_len[num%100]
        else:
            count_l = count_l + ones_len[int(num//100)] + hundred_len + and_len + tens_len[int(num%100//10 - 1)] + ones_len[int(num%10)]

print(count_l)
