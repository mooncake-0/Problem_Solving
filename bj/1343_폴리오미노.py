import sys

sys.stdin = open("input_1343.txt")

T = int(input())

for _ in range(T):

    tests = input()
    tests = tests.replace('XXXX', 'AAAA')
    tests = tests.replace('XX', 'BB')

    if 'X' in tests:
        print(-1)
    else:
        print(tests)
