import sys
from collections import deque

sys.stdin = open("input_2206.txt")
input = sys.stdin.readline

I, J = map(int, input().split())
maze = [list(map(str, input().strip())) for _ in range(I)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


'''
    포인트
    - 이런거좀 게시판 안보고 스스로 케치하고 싶다...
    - 반례를 조금만 더 섞어 봤으면 발견했을 것 같음 (그냥 열심히 막 만들어봐!) 
    - 내가 그 위치에 있을 수 있는게 (벽을 뿌쉈을 경우) 와 (안뿌수고 갔을 경우) 로 나뉘어지기 때문에
    - 반복 장소 갈 때 두 경우에 차이를 둬야 함. (broke_wall 을 나눠서 set 에 넣는다) 
    - 어려운거 다해놓고, 마지막 디테일에서 부족함.
'''
def print_maze(cur_pos, did_break_wall):
    print(cur_pos, " ", did_break_wall)

    for x in maze:
        print(x)
    print("================================")


def pro1():
    global maze
    dq = deque()
    dq.append(((0, 0), 1, False))
    visited = set()
    visited.add((0, 0, False))

    while dq:

        cur_pos, times, did_break_wall = dq.popleft()

        # print_maze(cur_pos, did_break_wall)

        if cur_pos == (I - 1, J - 1):
            print(times)
            return

        for i in range(4):
            mi = cur_pos[0] + di[i]
            mj = cur_pos[1] + dj[i]
            if 0 <= mi < I and 0 <= mj < J and (mi, mj, did_break_wall) not in visited:
                if maze[mi][mj] == "1" and not did_break_wall:  # 벽일 경우, 1회에 한하여 뚫을 수 있다
                    visited.add((mi, mj, True))
                    dq.append(((mi, mj), times + 1, True))  # 깼으면 True 로 전달

                elif maze[mi][mj] == "0":
                    visited.add((mi, mj, did_break_wall))
                    dq.append(((mi, mj), times + 1, did_break_wall))

    print(-1)


def main():
    pro1()


main()
