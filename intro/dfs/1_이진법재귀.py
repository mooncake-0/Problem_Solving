import sys


def transform(num):
    anw = ''
    while num > 0:
        a = num % 2
        num //= 2
        anw = str(a) + anw
    return int(anw)


num = int(input())
print(transform(num))
