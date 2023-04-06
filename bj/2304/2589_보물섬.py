import sys
from collections import deque

'''
포인트
 - 일일이 돌면서 전부 판단해야 겠다는 판단 - 50X50 인 것을 확인함으로써 얻을 수 있는 확신
 - 훼손되면 안되는 정보에 대한 판단
 - 굳이 global 로 두지 않고, 함수 내에 두어서 활용해도 됨 --> 이 부분에서 에러가 났었음
'''

input = sys.stdin.readline

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(position):  # 해당 지점으로 부터 bfs 를 돌린다
    global max_val
    eval = [[0] * J for _ in range(I)]

    dq = deque()
    dq.append((position, 0))
    eval[position[0]][position[1]] = 1

    while dq:
        cur_pos, cnt = dq.popleft()

        max_val = max(cnt, max_val)

        for k in range(4):
            mi = cur_pos[0] + di[k]
            mj = cur_pos[1] + dj[k]
            if 0 <= mi < I and 0 <= mj < J and treasureMap[mi][mj] == 'L' and eval[mi][mj] == 0:  # 아직 간 구간이 아닐경우
                dq.append(((mi, mj), cnt + 1))
                eval[mi][mj] = 1  # 갔음!


def main():
    global I, J, treasureMap, max_val
    I, J = map(int, input().split())
    treasureMap = [list(map(str, input().strip())) for _ in range(I)]

    # 돌면서 L인 지점을 만나면 BFS 를 시작한다
    # 참고로, 각 지점별로 모두 판단을 해야 한다 > BFS 가 종료되는 시점에서의 cnt 가 바로 제일 짧은 거리가 된다.
    # 이 때, 그 거리를 하나씩 저장한다. 그 거리가 제일 긴 두 지점 사이에 묻혀 있다. ( 그 거리가 답이다 )

    max_val = 0
    for i in range(I):
        # 하지만 계속 돌리면서 거리를 확인해야 하므로, treasureMap 은 훼손되면 안된다. (같은 배열 객체를 만든다음에 여기에 표시하자)
        for j in range(J):
            if treasureMap[i][j] == 'L':
                bfs((i, j))

    print(max_val)
    # L을 발견한 지점부터 그냥 다 돌린다


main()
