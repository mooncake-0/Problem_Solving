import sys
from collections import deque

sys.stdin = open("input_5.txt")

T = int(input())

for _ in range(1, T + 1):
    n, k = map(int, input().split())  # n 명의 왕자,  K 를 외침

    ''' 내 풀이
    raw = list(range(1, n + 1))
    cnt = 0
    while True:
        if len(raw) == 1:
            break
        else:
            removal = []
            for x in raw:
                cnt += 1
                if cnt == k:
                    removal.append(x)
                    cnt = 0
            for x in removal:
                raw.remove(x)
    print(raw[0])
    '''

    # 강사 풀이
    dq = list(range(1, n + 1))
    dq = deque(dq)
    cnt = 0
    while len(dq) != 1:
        cnt += 1
        if cnt != k:
            dq.append(dq.popleft())
        else:
            dq.popleft()
            cnt = 0
    print(dq.pop())