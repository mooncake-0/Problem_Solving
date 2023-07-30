import sys
from collections import deque

'''
s 9:45
e 10:40

같은 문제였어도 50분이나 걸리다니.. 
생각해 나가는 속도.. ㅠ
짜증나는 실수들 좀.. 하지 마라... 
나머진 잘했음
'''

sys.stdin = open("input_13460.txt")
input = sys.stdin.readline

I, J = map(int, input().split())
MAZE = [list(map(str, input().strip())) for _ in range(I)]

d_vector = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}  # 동남서북

for i in range(I):
    for j in range(J):
        if MAZE[i][j] == "R":
            red_position = (i, j)
        if MAZE[i][j] == "B":
            blue_position = (i, j)


def move_balls(red_pos, blue_pos, dir):
    red_fin = False
    blue_fin = False

    red_holled = False
    blue_holled = False

    while not red_fin or not blue_fin:
        # print("BEFORE:", red_pos, blue_pos, dir, red_fin, blue_fin)
        if not red_fin:
            mri = red_pos[0] + dir[0]
            mrj = red_pos[1] + dir[1]
        else:
            mri = red_pos[0]
            mrj = red_pos[1]

        if not blue_fin:
            mbi = blue_pos[0] + dir[0]
            mbj = blue_pos[1] + dir[1]
        else:
            mbi = blue_pos[0]
            mbj = blue_pos[1]

        extra_judge_needed = False  # 파란색 공까지 보고 판단해야함

        # 이제 움직여본다
        if not red_fin:

            ''' 벽이면 mri 로 최신화시키면 안됨'''
            if MAZE[mri][mrj] == "#":
                red_fin = True

            ''' 홀에 떨어지면 게임은 끝나지만, 이번 move 까지 blue ball 이 떨어지나 지켜봐야 한다'''
            if MAZE[mri][mrj] == "O":
                red_fin = True
                red_holled = True

            ''' 파란색 공의 상태를 고려해본다'''
            '''
            1) 파란색은 끝난 상태이다 > 내가 갈 위치가 파란색이면 안됨 > 파란색이면 최신화 시키면 안됨
            2) 파란색이 끝나지 않고 움직인다
            > 내가 갈 위치가 기존 파란색 위치와 같다면 
                                        > 이번 파란색이 정지될 것이다 (빨간색도 정지) > 최신화시키면 안됨
                                        > 이번 파란색이 움직일 수 있다 (빨간색도 그대로 움직인다)
            > 아니면 그냥 알아서 움직임 
            '''
            if not red_fin:  # 지금까지 정지되지 않았다면
                if blue_fin:
                    if (mri, mrj) == blue_pos:
                        red_fin = True
                else:
                    if (mri, mrj) == blue_pos:
                        extra_judge_needed = True

        ''' 이제 파란색을 본다'''
        if not blue_fin:
            ''' 벽이면 mri 로 최신화시키면 안됨'''
            if MAZE[mbi][mbj] == "#":
                blue_fin = True
                if extra_judge_needed:  # 이 CASE 면 red 역시 최신화되면 안됨
                    red_fin = True

            ''' 홀에 떨어지면 어떤 경우이든 이번 CASE는 실패이다'''
            if MAZE[mbi][mbj] == "O":
                blue_fin = True
                blue_holled = True

            ''' 이제 파란색의 이동 상태 분석'''
            '''
            1) 빨간색이 red_fin 이면 이동을 완료한 상태
            '''
            if not blue_fin:
                if red_fin and not red_holled:  # 빨간색이 들어갔으면, red_pos 은 움직였어야 하므로
                    if (mbi, mbj) == red_pos:  # 가려고 하는 곳에 빨간색이 위치한다면
                        blue_fin = True  # red 가 원래 끝나있으면, red_pos 은 변경하지 않고, 이번에 끝났어도 red_pos 이 실제 위치임
                # red_not_fin 이라면, red는 움직임을 완료한 상태이다
                # 기존경로에 red가 있든 없든 그냥 움직여도 된다는 뜻이므로, 그대로 간다

        ''' 최신화를 결정한다 '''
        if not red_fin or red_holled:  # 이번을 통해 움직이지 않아야 하면, 최신화 하지 않는다 (하지만 홀에 빠진거면 마지막 최신화는 해줘야 한다)
            red_pos = (mri, mrj)
        if not blue_fin or blue_holled:
            blue_pos = (mbi, mbj)

        # print("AFTER:", red_pos, blue_pos, dir, red_fin, blue_fin)

    if blue_holled:
        return -1  # 무조건 실패임
    if red_holled:
        return 1  # blue 가 안들어갔으면 성공이므로

    # 둘다 아니면 움직였음
    return (red_pos, blue_pos)


def pro1():
    dq = deque()
    dq.append((red_position, blue_position, 0))

    visited_positions = set()
    visited_positions.add((red_position, blue_position))

    while dq:

        c_rp, c_bp, times = dq.popleft()
        if times == 10:
            break
        for i in range(4):
            tmp = move_balls(c_rp, c_bp, d_vector[i])
            if tmp == 1:
                return times + 1
            elif tmp == -1:
                pass
                # print("실패! 다음 rounding")
            else:  # 다음 움직임 장소들이 결정됨
                # print("TRYING", tmp[0], tmp[1], times + 1)
                if (tmp[0], tmp[1]) in visited_positions:
                    # print("ALREADY CONSIDERED")
                    continue
                dq.append((tmp[0], tmp[1], times + 1))
                visited_positions.add((tmp[0], tmp[1]))

    return -1


def main():
    print(pro1())


main()
