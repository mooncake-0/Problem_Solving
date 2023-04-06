import sys
from collections import deque

sys.stdin = open("input_2412.txt")
input = sys.stdin.readline


def judge_available(s_pos, n_pos):
    if abs(n_pos[0] - s_pos[0]) > 2:
        return False
    if abs(n_pos[1] - s_pos[1]) > 2:
        return False
    if used == 1:
        return False
    return True


def main():
    s = (0, 0)
    dq = deque()
    dq.append((s,0))

    while dq:

        cur_pos, cnt = dq.popleft()

        if cur_pos[1] >= T:
            print(cnt)
            return

        for i in range(len(homes)):
            next_pos = homes[i]
            if next_pos[0] - cur_pos[0] > 2:
                break
            else:
                if judge_available(cur_pos, next_pos):
                    used[i] = 1
                    dq.append((next_pos, cnt+1))
    print(-1)


N, T = map(int, input().split())
used = [0] * N  # 사용된 곳 표시해주기
homes = []  # len = 50000 * 15 정도
for _ in range(N):
    a = tuple(map(int, input().split()))
    homes.append(a)

homes.sort() # x 좌표 기준으로 정렬된다
# print(homes)

main()
