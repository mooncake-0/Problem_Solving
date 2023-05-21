import sys
from collections import deque

sys.stdin = open("input_4179.txt")
input = sys.stdin.readline

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
I, J = map(int, input().split())

'''
약간의 구현 + BFS 였음
포인트
    - (중요) 무조건 BFS 인데 메모리/시간 초과 나면 중복 데이터들이 많이 발생하고 있음을 염두! (그럼에도 안되면.. 방향 틀린거..) 
    - BFS 에서 depth 에 대한 판단하는 경험! (전달하면서 몇번째 depth 인지를 판별하며 진행한다) 
'''


maze = []  # I, J = 1000, 10000 >> 1000 * 1000 = 1,000,000 # 이렇게 되면
visited = [[0] * J for _ in range(I)]
f_dq = deque()
for i in range(I):
    tmp = list(map(str, input().strip()))
    for j in range(J):
        if tmp[j] == 'J':
            jp = (i, j)
            tmp[j] = '.'

        if tmp[j] == 'F':
            f_dq.append((i,j))
    maze.append(tmp)


def print_maze(cjp):
    for x in maze:
        print(x)
    print(cjp)
    print("============================")


# J > 지훈이 첫 위치
# F > 불 시작 위치 >> 상하좌우로 확산됨
# # > 고정 벽
def pro1():
    global visited

    j_dq = deque()
    j_dq.append((jp, 0))

    cur_cnt = 0

    while j_dq:


        cjp, cnt = j_dq.popleft()

        # 현 시점 기준에서 > 불이 번진다 > 지훈이가 이동할 장소를 찾는다
        # cnt 가 바뀌었으면, 불을 움직이고, 그 움직인 기점으로 지훈이가 이동할 장소를 찾아야 한다
        if cnt == 0 or cur_cnt + 1 == cnt:  # 증가하는 시점이 옴 > 불을 움직인 다음에 지훈이가 이동할 장소를 찾아야 함
            if cur_cnt +1 == cnt:
                cur_cnt += 1
            for i in range(len(f_dq)):  # 4개면 4번 진행한다

                cfp = f_dq.popleft()

                for j in range(4):
                    # 각 포지션 별로 상하좌우를 판별함
                    mi = cfp[0] + di[j]
                    mj = cfp[1] + dj[j]

                    if 0 <= mi < I and 0 <= mj < J:  # 범위 안이며
                        if maze[mi][mj] == '.':  # 움직임이 가능한 위치이다 (지훈이도 이번에 움직여야 하기 때문)
                            maze[mi][mj] = 'F'  # 그리고 이 친구들은 다음에 번져야할 대상이 된다
                            f_dq.append((mi, mj))

        # 이제 지훈이가 움직인다
        for i in range(4):
            mi = cjp[0] + di[i]
            mj = cjp[1] + dj[i]
            if 0 <= mi < I and 0 <= mj < J and maze[mi][mj] == '.' and visited[mi][mj] == 0:  # 갈 수 있는 곳이 있다면
                # BFS 추가
                visited[mi][mj] = 1
                j_dq.append(((mi, mj), cnt + 1))
            if 0 > mj or J <= mj or 0 > mi or I <= mi:  # 벗어날 수 있다면
                # 종료
                print(cnt + 1)
                return

    print("IMPOSSIBLE")


def main():
    pro1()


main()
