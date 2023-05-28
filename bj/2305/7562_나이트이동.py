import sys
from collections import deque

sys.stdin = open("input_7562.txt")
input = sys.stdin.readline

di, dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(cur_knight, tg_pos):
    global N
    visited = set()
    dq = deque()
    dq.append((cur_knight, 0))

    while dq:
        cur_pos, moved = dq.popleft()

        if cur_pos == tg_pos:
            return moved

        for i in range(8):
            mi = cur_pos[0] + di[i]
            mj = cur_pos[1] + dj[i]
            if 0 <= mi < N and 0 <= mj < N and (mi, mj) not in visited:
                visited.add((mi, mj))
                dq.append(((mi, mj), moved + 1))


def main():
    global N
    TC = int(input())
    for _ in range(TC):
        N = int(input())
        cur_knight = tuple(map(int, input().split()))
        tg_pos = tuple(map(int, input().split()))
        print(bfs(cur_knight, tg_pos))


main()
