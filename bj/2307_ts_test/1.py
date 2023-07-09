import sys

sys.stdin = open("input_1.txt")
input = sys.stdin.readline


def check(check, N):
    for i in range(1, N + 1):
        if i not in check:
            return False
    return True


def solution(s, N):  # N : 1 ~ 9
    anw = -1
    for i in range(len(s) - (N - 1)):
        tmp_set = set()
        for j in range(i, i + N):
            tmp_set.add(int(s[j]))
        isIt = check(tmp_set, N)
        if isIt:
            anw = max(anw, int(s[i:i + N]))
    return anw


s = input().strip()
N = int(input())
print(solution(s, N))
