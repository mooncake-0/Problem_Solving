import sys
from collections import deque
'''
포인트
 - 움직임에 대한 모든 판단이 필요. 중간에 말이 가로막고 있으면 못간다. 
 - 왕이 막고 있으면 못간다 (쓸데 없는 조건은 절대 주어지지 않는다) 
 - 다행히 세번째 TC 에서 확인할 수 있는 문제 ( 착한 문제 ) 
'''
input = sys.stdin.readline

# 경로에 대해 판단하려면 움직이는 경로들까지 추가된 상태여야 한다
di, dj = [(0, -1, -1), (0, 1, 1), (1, 1, 1), (1, 1, 1), (0, -1, -1), (0, 1, 1), (-1, -1, -1), (-1, -1, -1)], [(1, 1, 1),(1, 1, 1),(0, 1, 1),(0, -1,-1), (-1,-1,-1), (-1,-1,-1), (0, -1,-1),(0, 1, 1)]


def pro1():
    global board, e
    cnt = 0
    dq = deque()
    dq.append((e, cnt))

    while dq:
        cur_pos, cnt = dq.popleft()

        for l in range(8):
            # 한 항목 안에서 3번 움직이는 동안에 대해서도 판단을 해줘야 함
            moving_x = cur_pos[0]
            moving_y = cur_pos[1]

            for k in range(3):
                moving_x += di[l][k]
                moving_y += dj[l][k]
                # 경로가 부합하는지 판단할 것임
                if (0 <= moving_x < 10) and (0 <= moving_y < 9):  # 범위가 되는 애들 중에

                    if k != 2:  # 가는 길일 때면 판단만 해준다
                        if board[moving_x][moving_y] == 2:  # 가는길에 왕이 있음
                            break  # 얘는 안되는 loop, 다른 이동경로 탐색한다

                    else:  # 최종 도착지에서
                        if board[moving_x][moving_y] != 1:  # 갔던 곳만 아니면 ㄱㅊ은데 왕이면 끝 아님?
                            if board[moving_x][moving_y] == 2:  # 2이면 끝임
                                print(cnt + 1)  # 다음 도착 예정지이므로
                                return
                            else:
                                dq.append(((moving_x, moving_y), cnt + 1))
                                board[moving_x][moving_y] = 1  # 여기서 체크를 해놔야, 다음에 도는 애가 얘를 봤을 때 "아 이미 deq 에 있구나" 할 수 있음
    # 더이상 돌 곳이 없으면 종료한다
    print(-1)


def main():
    global board, king, e
    board = [[0] * 9 for _ in range(10)]  # 움직인 곳은 1 로 변경 // 움직이지 못한 곳은 갈 수 없단 조건은 없지만, 없어야 무한 loop 에 안빠짐
    ea, eb = map(int, input().split())
    ka, kb = map(int, input().split())
    e = (ea, eb)
    board[ea][eb] = 1
    board[ka][kb] = 2
    pro1()


main()
