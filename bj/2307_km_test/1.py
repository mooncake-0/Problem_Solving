import sys

sys.stdin = open("input_1.txt")
input = sys.stdin.readline

def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print != 1 and N % 10 != 0:
            enable_print = 1
        if enable_print == 1:
            print(N % 10, end="")
        N = N // 10

TC = int(input())
for _ in range(TC):
    numb = int(input())
    solution(numb)
    print()