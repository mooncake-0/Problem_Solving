import sys
from collections import deque

'''
s 9:33   
e 11:03  

- 생각 자체가 좀 더 빠르면 좋을 것 같은데 .. (이건 매번 느낀다. 좀 긴박감을 가지고 해보자)
- 탐색은 일단 한바퀴 돌아보는게 중요한듯! 돌리고 상황을 해결해 나가는 것 (printing logging 잘하기)
- 발생하지 않을 상황을 판단, 여러가지 케이스 판단, 복잡한 상황이더라도 어떻게 구현할 수 있을지 나아가는건 ㄱㅊ았던 듯
- 예제7에서 빼먹은 CASE 를 발견, 해결하기 위한 적용까지 잘 해나갔음
- 다만, 좀 더 자신감을 가지고 했으면 좋겠음
'''

sys.stdin = open("input_13459.txt")
input = sys.stdin.readline

I, J = map(int, input().split())
MAZE = [list(map(str, input().strip())) for _ in range(I)]

for i in range(I):
    for j in range(J):
        if MAZE[i][j] == 'R':
            red_position = (i, j)
        if MAZE[i][j] == 'B':
            blue_position = (i, j)

# 동, 남, 서, 북 순서로 0,1,2,3
d_vector = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}


def move_balls(r_ball, b_ball, dir):
    # dir = (x,y) 결정된 상태
    rb_fin = False
    bb_fin = False
    red_ball_in = False
    blue_ball_in = False

    # (1,4),(1,5) dir (0,-1)
    while not rb_fin or not bb_fin:

        ''' 움직임이 끝난상태라면 멈춰두고, 시도해야 하는 상황이라면 움직여 본다'''
        if not rb_fin:
            mi_r_ball = r_ball[0] + dir[0]
            mj_r_ball = r_ball[1] + dir[1]
        else:
            mi_r_ball = r_ball[0]
            mj_r_ball = r_ball[1]

        if not bb_fin:
            mi_b_ball = b_ball[0] + dir[0]
            mj_b_ball = b_ball[1] + dir[1]
        else:
            mi_b_ball = b_ball[0]
            mj_b_ball = b_ball[1]

        # print("red hello", mi_r_ball, mj_r_ball)
        # print("blue hello", mi_b_ball, mj_b_ball)

        ''' 볼은 각각 제어한다 '''
        ''' 레드볼 먼저'''
        judge_needed = False

        if not rb_fin:

            '''가려는 곳이 벽이다'''
            if MAZE[mi_r_ball][mj_r_ball] == "#":
                rb_fin = True

            ''' 가려는 곳이 0 이면 성공시그널을 준다'''
            if MAZE[mi_r_ball][mj_r_ball] == "O":
                rb_fin = True # 더이상 움직이진 않을 것임
                r_ball = (mi_r_ball, mj_r_ball)# 하지만 이번 포지션은 업데이트 해줄 것임
                red_ball_in = True

            ''' 가려는 곳에 파란 볼이 있을 때 파란색 볼의 움직임에 대하여 '''
            # 1번 상황 : 파란볼은 종료되었고, 가는 곳에 파란 볼이 있을 때
            # 2번 상황 : 파란불 미종료 / 내가 가려는 곳이 파란불의 기존 위치 (파란불 다음 장소 확정 X)
            #         : 파란불 미종료 / 파란불이 갈 경우 이동 가능하지만, 불가능으로 판별났을 떄 돌아와야 함
            #         : 파란불 미종료 / 아무 상관 없이 움직임
            if not rb_fin: # 아직 종료되지 않았다면
                if bb_fin: # 파란불은 다음 움직임이 없을 때
                    if (mi_r_ball, mj_r_ball) == (mi_b_ball, mj_b_ball): # 가려는 길에 파란볼이 있음
                        rb_fin = True
                else:
                    if (mi_r_ball, mj_r_ball) == b_ball:
                        judge_needed = True

        if not bb_fin: # 파란볼도 움직였음

            '''가려는 곳이 벽이다'''
            if MAZE[mi_b_ball][mj_b_ball] == "#":
                bb_fin = True
                if judge_needed: # 이 상황 때문에 체크해준거긴 함
                    rb_fin = True # rb 도 움직여주지 않는다

            ''' 가려는 곳이 0 이면 성공시그널을 준다'''
            if MAZE[mi_b_ball][mj_b_ball] == "O":
                bb_fin = True
                blue_ball_in = True

            if not bb_fin: # 아직 종료되지 않았다면
                if rb_fin:
                    if (mi_b_ball, mj_b_ball) == r_ball: # 가려는 길에 빨간볼이 있음
                        bb_fin = True

        # 다 통과한 후에도 끝나지 않았으면 그 외의 상황 = 포지션을 업데이트한다
        if not rb_fin:
            r_ball = (mi_r_ball, mj_r_ball)
        if not bb_fin:
            b_ball = (mi_b_ball, mj_b_ball)

    # 이번 시도가 종료된 상태에서
    if red_ball_in: # 빨간 공이 들어간 상태다
        if blue_ball_in: # 근데 파란 공도 들어갔따
            return -1
        else:
            return 1
    if blue_ball_in:
        return -1

    return (r_ball, b_ball)

# 차피 모든 탐색 다해야함, 하나만 나오면 1로 가능
# 1번당 4번의 움직임 > 10 번 =4 ^ 10 = 2^20 = 1024 * 1024 = 1,048,576 > 부담되는 수준 X
def pro1():
    dq = deque()
    dq.append((red_position, blue_position, 0))
    visited_position = set()
    visited_position.add((red_position, blue_position))
    while dq:
        c_rp, c_bp, times = dq.popleft()
        # print("Starting")
        # print(c_rp, c_bp, times)
        if times == 10:  # 10번째로 움직인 이후이다.
            return 0

        # 네 방향대로 모두 움직인다. 한번 움직이면 끝까지 가는거다
        for i in range(4):
            tmp = move_balls(c_rp, c_bp, d_vector[i])
            if tmp == 1: # 성공했다.
                return 1
            elif tmp == -1: # 실패했다.
                # print(d_vector[i], " not working")
                pass
            else: # 제대로 위치가 반환이 되었다
                # print(d_vector[i], "ends:: ", "moved to", tmp)
                if tmp in visited_position:
                    # print("already considered :  not appending to deq")
                    continue
                dq.append((tmp[0], tmp[1], times+1))
                visited_position.add((tmp[0], tmp[1]))

    # 10 번 넘기기도 전에 모든 경우가 소진됨
    return 0

def main():
    anw = pro1()
    print(anw)


main()
