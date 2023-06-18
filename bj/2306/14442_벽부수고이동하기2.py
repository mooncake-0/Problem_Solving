import sys
from collections import deque

sys.stdin = open("input_14442.txt")
input = sys.stdin.readline

'''
포인트
 - 문제가 쫌 짜증났음
 - a 에 벽이 있고, 내가 a 1번으로 벽을 뚫고 a+1 번으로 갔으면, a+1 에서 탐색할때 2번째로 다시 a 번 벽을 뚫을 수 있음 (왜냐면 그리고 maze 에 뚫린 벽이라고 표시도 안함)
 - 왜냐하면 1번 으로 뚫었을 상황만 지나갔다고 표기되어 있기 때문 >> 이걸 고려하지 않아도 답이 되는게 좀 ㅈ같음
 - (그만큼 시간과 용량을 넉넉히 잡아준듯) 
 - 가정: 내가 M 만큼 뚫은 상태에서 (mi,mj) 에 도달했으면, 어떤 길을 뚫고 왔든 이 상황에 도달하면 더 이상 그 경우는 DQ에 포함시키지 않아도 된다.
 - 왜냐하면 이 이후로 어떻게 가든 똑같을 것이기 때문이다.
 - 그리고 maze 를 visited_maze 에 copy 시켜서 같은 참조값을 가져서 동기화 되어버리는 현상도 있었음
 - visited_maze 는 굳이 maze 모습을 반영할 필요가 없었음
 - 암튼.. 좀 찝찝한 문제.

'''

# N, M 1~ 1000 (꽤 큼)
I, J, K = map(int, input().split())
maze = [list(map(str, input().strip())) for _ in range(I)]
visited_maze = [[[0] * J for _ in range(I)] for _ in range(K + 1)]  # 그 층에서 거기를 지났을까?
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def print_status(dq):
    for k in range(K + 1):
        for x in visited_maze[k]:
            print(x)
        print("--------")
    print(dq)
    print("===============================")


def pro1():
    global visited_maze
    dq = deque()
    dq.append(((0, 0), 1, 0))
    visited_maze[0][0][0] = -1

    while dq:

        cur_pos, times, break_used = dq.popleft()
        # print(cur_pos, times, break_used)
        # print_status(dq)

        if cur_pos == (I - 1, J - 1):
            return times

        # 이동을 수행한다
        for k in range(4):
            mi = cur_pos[0] + di[k]
            mj = cur_pos[1] + dj[k]
            if 0 <= mi < I and 0 <= mj < J and maze[mi][mj] == '0' and visited_maze[break_used][mi][mj] != -1:
                # 여기서 횟수 더하기를 한다
                visited_maze[break_used][mi][mj] = -1
                dq.append(((mi, mj), times + 1, break_used))

            elif 0 <= mi < I and 0 <= mj < J and maze[mi][mj] == '1' and break_used < K:
                if visited_maze[break_used + 1][mi][mj] != -1:
                    visited_maze[break_used + 1][mi][mj] = -1  # 지났다고 표기
                    dq.append(((mi, mj), times + 1, break_used + 1))  # break 를 한번 더 썼다고 표기

    return -1


def main():
    print(pro1())


main()
