import sys

sys.stdin = open("input_1.txt")
input = sys.stdin.readline


def numb_cnt(number):  # 자릿수 반환
    return len(str(number))


def print_top(line_cnt, col_cnt):
    for i in range(col_cnt):
        print("+" + "-" * line_cnt, end="")
    print("+")


def print_numbs(line_cnt, numbs):
    # print(line_cnt)
    for i in range(len(numbs)):  # K 번 진행
        space_cnt = line_cnt - len(str(numbs[i]))
        # print(space_cnt)
        print("|" + " " * (space_cnt) + str(numbs[i]), end="")
    print("|")


def solution(A, K):
    max_int = max(A)
    longest_numb_cnt = numb_cnt(max_int)

    # 일단 기본적으로 4개 이상일때와
    if len(A) >= K:
        while len(A) >= K:
            numbs = A[:K]
            print_top(longest_numb_cnt, K)
            print_numbs(longest_numb_cnt, numbs)
            A = A[K:]
        print_top(longest_numb_cnt, K)  # 어쩄든 끝났다는 것
        if A:  # 남아있으면 출력
            print_numbs(longest_numb_cnt, A)
            print_top(longest_numb_cnt, len(A))
    # 초장부터 4개 미만일때를 나눠주면 좋을 듯
    else:  # 그냥 바로 끝내면 됨
        print_top(longest_numb_cnt, len(A))
        print_numbs(longest_numb_cnt, A)
        print_top(longest_numb_cnt, len(A))


A = list(map(int, input().split()))
K = int(input())
solution(A, K)
