import sys

sys.stdin = open("input_test.txt")
input = sys.stdin.readline


# 그냥 1 부터 시작해서 순서대로 나열
def sol(A):
    a_set = set(A)
    j = 1
    while j <= 100_000:
        if j not in a_set:
            return j
        j += 1
    return 100_001


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(sol(arr))
