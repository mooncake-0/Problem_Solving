from itertools import combinations
import sys
from collections import deque

'''
set 을 더할땐 update, set 을 더해서 새로운 set 반환시는 union


'''
sys.stdin = open("input_11559.txt")
open = sys.stdin.readline

I, J = 12, 6
puyo = [list(map(str, input().strip())) for _ in range(I)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(cur_position, color):
    dq = deque()
    dq.append(cur_position)  # 붙어있는 수

    is_blowing = False

    blow_set = set()
    blow_set.add(cur_position)

    is_attaching = 1

    while dq:

        position = dq.popleft()

        if is_attaching >= 4:
            is_blowing = True

        for k in range(4):
            mi = position[0] + di[k]
            mj = position[1] + dj[k]

            if 0 <= mi < I and 0 <= mj < J and puyo[mi][mj] == color and (mi, mj) not in blow_set:
                is_attaching += 1
                dq.append((mi, mj))
                blow_set.add((mi, mj))

    if not is_blowing:
        blow_set.clear()

    return blow_set


def pull_col(position):
    # position 이 broken 으로 지정되었다.
    # position[1] 의 열에서, position[0] 의 행들이 하나씩 당겨질 예정
    # 0 ~ position[0] 까지
    for i_idx in range(position[0], -1, -1):  # 0행부터 position[0] 행까지
        if i_idx == 0:
            puyo[i_idx][position[1]] = '.'
        else:
            puyo[i_idx][position[1]] = puyo[i_idx - 1][position[1]]


# 쭉 읽으면서 깰 수 있는 모델들을 일단 다 깬다
def main():
    global combo
    while True:

        blowers = set()
        for i in range(I):
            for j in range(J):
                if puyo[i][j] != '.' and (i, j) not in blowers:
                    blow_set = bfs((i, j), puyo[i][j])
                    if blow_set:  # empty 가 아니라면, 이번 round 에서 깨질 애들로 추가된다
                        blowers.update(blow_set)

        if not blowers: # blow 할 애들이 없으면 종료된다
            break

        combo += 1

        # 완료된 blowers 를 가지고 깬 후에 전체 이동을 진행
        for pos in blowers:
            puyo[pos[0]][pos[1]] = 'b'

        # 다시 전체를 읽으면서 b를 만나는 순간마다 제거후 해당 열을 당겨준다
        for i in range(I):
            for j in range(J):
                if puyo[i][j] == 'b':
                    pull_col((i,j))

combo = 0
main()
print(combo)
