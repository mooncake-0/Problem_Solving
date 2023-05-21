import sys
from collections import deque

sys.stdin = open("input_2178.txt")
input = sys.stdin.readline

I, J = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(I)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

# 걍 도달할때까지 BFS 돌리는것일듯
def pro1():
    global maze

    # 현재 포지션 (1,1)
    # 움직임이 몇 번째 인지도 감지해야한다
    cp = (0, 0)
    dq = deque()
    dq.append((cp, 1))  # 한칸 먹음
    maze[0][0] = 0  # 먹었음을 표시

    while dq:

        cur_pos, cnt = dq.popleft()
        # 종료지점인지 판단
        # 쭉 돌면서 갈 수 있는 지점 확인, 간 곳은 또 가지 않는다
        if cur_pos == (I - 1, J - 1):
            print(cnt)
            return

        for i in range(4):
            mi = di[i] + cur_pos[0]
            mj = dj[i] + cur_pos[1]
            if 0 <= mi < I and 0 <= mj < J and maze[mi][mj] == 1:
                maze[mi][mj] = 0  # 미리 가는 지점으로 넣어줘야, 다음에 주변에서 돌 떄 또 안넣어진다.
                dq.append(((mi, mj), cnt + 1))


def main():
    pro1()


main()