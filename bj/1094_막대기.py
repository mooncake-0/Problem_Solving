import sys


def transform(num):
    anw = ''
    while num > 0:
        a = num % 2
        num //= 2
        anw = str(a) + anw
    return anw


sys.stdin = open("input_1094.txt")
T = int(input())
for _ in range(T):
    num = int(input())
    cnt = 0
    for x in transform(num):
        if x == '1':
            cnt += 1
    print(cnt)
