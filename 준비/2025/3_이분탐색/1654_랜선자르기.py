import sys


def checker(tg, K, lines):
    sum = 0
    ## ㅋㅋㅋㅋ 진짜 ㅂㅅ이다.. 그냥 몇번 나눠지는지 하면 됨..
    for a in lines:
        # while a - tg >= 0:
        #     sum += 1
        #     a -= tg
        sum += a//tg
    if sum < K:
        return False
    return True


def solution(N, K, lines):
    # 범위 설정: 0 이면 안되고, 1,000,000 이면 안됨
    st = 0
    end = 2 ** 31
    while st + 1 < end:
        mid = (st + end) // 2
        if checker(mid, K, lines):  # 11개이거나 넘어서 True -> tg 을 조금 더 넓게 잡아도 된다
            st = mid  # tg 을 올려야 하기 때문에
        else:
            end = mid
    # 경계 지점 st+1 == end ( st, 4 end 5 여도 루프 탈출하기 때문)
    return st


sys.stdin = open("input_1654.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
lines = []

for _ in range(N):
    lines.append(int(input()))

print(solution(N, K, lines))
