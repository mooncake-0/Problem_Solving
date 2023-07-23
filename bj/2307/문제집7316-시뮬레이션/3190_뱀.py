import sys
from collections import deque

'''
s : 8:05 
e : 9:32
... 골드4 구현 정도를 1시간 30분 걸리면 안되는 듯
--- 틀려가지고 30분 더 잡아먹음.. 1시간도 오래 걸린건데.. 
--- 일단 구현은 했는데
--- tail 도 끝난 뒤에 움직여야 했는데 tail 은 동시에 움직였음. <= time 에서 < time 으로 수정 (9초가 끝난뒤에 방향 전환이 이루어져야 하면 10초 시작할 때 방향전환과 같음)
'''
sys.stdin = open("input_3190.txt")
input = sys.stdin.readline

# 벽 또는 자신과 부딪히면 끝
N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
p = int(input())
tmp = [tuple(map(str, input().split())) for _ in range(p)]
dir_change = dict()
for x in tmp:
    dir_change[x[0]] = x[1]

dir = 0  # 0123 > 동남서북
dir_vector = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
length = 1

def maze_print():
    for x in maze:
        print(x)
    print("==-=-")

def pro1():
    global maze, length, dir

    cur_head_position = (0, 0)
    cur_tail_position = (0, 0)
    tail_dir_change = deque()
    tail_dir = dir

    time = 1
    while True:
        '''방향대로 움직임'''
        mi = cur_head_position[0] + dir_vector[dir][0]
        mj = cur_head_position[1] + dir_vector[dir][1]

        '''maze 밖을 나갈 시 종료'''
        if 0 > mi or N <= mi or 0 > mj or N <= mj:
            break

        cur_head_position = (mi, mj)  # 얘는 움직임

        if maze[mi][mj] == 2:
            # 먹으면 자란다 # end_position 유지
            length += 1
            # 먹으면 tail 움직임도 1초 뒤에 움직여야 한다
            for k in tail_dir_change:
                k[0] += 1

        elif maze[mi][mj] == 0: # Tail 움직임에 관하여
            ''' dir_change 해야 한다면, 한다 '''
            if tail_dir_change and tail_dir_change[0][0] < time:  # 현재 바꿔야 하는 time 이 넘었다면
                if tail_dir_change[0][1] == 'L':
                    tail_dir -= 1
                    if tail_dir == -1:
                        tail_dir = 3
                else:
                    tail_dir += 1
                    if tail_dir == 4:
                        tail_dir = 0
                tail_dir_change.popleft()  # 제거해줌
            # print(tail_dir, cur_tail_position)
            '''tail 을 움직여준다'''
            ti = cur_tail_position[0] + dir_vector[tail_dir][0]
            tj = cur_tail_position[1] + dir_vector[tail_dir][1]

            ''' 기존 포지션은 0으로 바꿔준다'''
            maze[cur_tail_position[0]][cur_tail_position[1]] = 0
            cur_tail_position = (ti,tj)

        else:  # 1일경우 부딪힌 것이므로 종료
            break

        maze[mi][mj] = 1

        '''time 초가 끝난 뒤 방향 전환 로직'''
        if str(time) in dir_change:
            if dir_change[str(time)] == 'L':
                dir -= 1
                if dir == -1:
                    dir = 3
            else:
                dir += 1
                if dir == 4:
                    dir = 0
            # 이 때, tail 에게도 L-1 초 뒤에 바뀌어야 함을 알려준다 #L = 1 이면 나도 바꿔야함
            tail_dir_change.append([time + length - 1, dir_change[str(time)]])

        # print(time)
        # print(tail_dir_change)
        # maze_print()

        time += 1
    print(time)

def main():
    global maze
    maze = [[0] * N for _ in range(N)]
    for pos in apples:
        maze[pos[0] - 1][pos[1] - 1] = 2  # 사과 위치 표시
    maze[0][0] = 1  # 애벌레 위치 표시
    pro1()


main()