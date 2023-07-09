import sys

sys.stdin = open("input_ex.txt")
input = sys.stdin.readline


def solution(s):
    anw = -1
    for i in range(len(s) - 2):
        numb = int(s[i])
        for j in range(i, i + 3):
            if int(s[j]) != numb:
                break
            else:
                if j == i + 2:
                    temp = s[j] + s[j] + s[j]
                    anw = max(anw, int(temp))
                continue
    return anw


N = input().strip()
print(N)
print(solution(N))
