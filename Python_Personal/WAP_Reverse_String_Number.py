def reverseNumber(n=123):
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = int(n / 10)

    return reverse


print(reverseNumber(1234))


def reverseString(st='tluafed'):
    return st[::-1]


print(reverseString('friends'))
