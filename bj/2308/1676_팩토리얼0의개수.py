import sys

sys.setrecursionlimit(1000)
sys.stdin = open("input_1676.txt")
input = sys.stdin.readline

N = int(input())

def recursive(N):
    if N == 1:
        return 1
    else:
        return recursive(N-1) * N


def count_zero(number):
    count = 0
    while number % 10 == 0:
        count += 1
        number = number // 10
    return count

print(count_zero(recursive(N)))
