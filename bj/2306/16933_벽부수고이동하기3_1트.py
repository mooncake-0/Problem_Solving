import sys
from collections import deque

sys.stdin = open("input_16933.txtw")
input = sys.stdin.readline

I, J, K = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(I)]  # 고정 MAP 정보 (변경X)
visited_maze = [[[0] * J for _ in range(I)] for _ in range(K + 1)]  # 몇 번째로 부쉈는지에 대한 탐색 정보

# 기존 자리를 고수해도 된다 ( 하나 추가 )
di, dj = [0, 1, 0, -1, 0], [1, 0, -1, 0, 0]


def print_status(dq):
    for k in range(K + 1):
        for x in visited_maze[k]:
            print(x)
        print("--------------")
    print(dq)
    print("======================================================")

def pro1():
    dq = deque()
    dq.append(((0, 0), 1, 0, True))  # cur_position(i,j), moved, break_used, is_day # moved 횟수가 올라갈 때마다 낮 / 밤 이 바뀐다
    visited_maze[0][0][0] = -1

    # 칸에 머무를 수 있음
    while dq:

        cur_position, moved, break_used, is_day = dq.popleft()

        if cur_position == (I - 1, J - 1):
            return moved

        for k in range(5):
            mi = cur_position[0] + di[k]
            mj = cur_position[1] + dj[k]

            if 0 > mi or I <= mi or 0 > mj or J <= mj:  # 제한 범위를 초과하면 out
                continue

            '''존버하는 경우는, 낮이나 밤이 바뀌어서 벽을 부수기 위함인데, 두번 이상 존버할 필요가 없을 것 같다 - 한번만 존버를 허용함'''
            # 그냥 지나다닐 경우 # 일단 갈 수 있고, 간 적이 없을 때 (하지만 머무르는거라면 통과시켜준다, 이미 자기 위치가 -1 일지라도)
            if maze[mi][mj] == 0 and (visited_maze[break_used][mi][mj] != -1 or (mi, mj) == cur_position):
                if visited_maze[break_used][mi][mj] == -2:  # 존버를 이미 한 위치
                    pass
                else:  # 일반 case - 간 적이 없다. 존버 1차 시도이다
                    if (mi, mj) == cur_position and not is_day:  # 존버 1차 시도시
                        visited_maze[break_used][mi][mj] = -2
                    else:  # 일반 case
                        visited_maze[break_used][mi][mj] = -1
                    dq.append(((mi, mj), moved + 1, break_used, not is_day))

            # 벽일 경우 부셔서 들어갈 수도 있다
            elif maze[mi][mj] == 1:
                ''' 그렇다기보단 존버를 해보려 하는거임'''
                if (mi, mj) == cur_position:  # 지금 자리에 있으면 더 부술 필요는 없음, break_used ==K 여도 ㄱㅊ음
                    if visited_maze[break_used][mi][mj] == -2:  # 존버를 더할 필요는 없음
                        pass
                    else:  # -2 가 아니면 첫 존버임 # 밤에만 하는게 좋지 않겠음? > 존버 이유가 낮밤 때문임
                        if not is_day:
                            visited_maze[break_used][mi][mj] = -2  # 어차피 -1 이긴 할 것임
                            dq.append(((mi, mj), moved + 1, break_used, not is_day))

                else:
                    ''' 일반적으로 벽을 부쉈을 경우'''
                    if is_day and break_used < K and visited_maze[break_used + 1][mi][mj] != -1 and visited_maze[break_used+1][mi][mj] != -2:
                        visited_maze[break_used + 1][mi][mj] = -1  # 그자리에 부수고 가겠다
                        dq.append(((mi, mj), moved + 1, break_used + 1, not is_day))

    return -1


def main():
    print(pro1())
    # print(pro2())



main()
