import sys
from collections import deque

sys.stdin = open("input_16933.txt")
input = sys.stdin.readline

'''
포인트
 - 벽부이2 문제와 동일하게, 특정 상황에 대해서는 고려를 안해준 case
 - "하루 버티는 이유" 에 대해서 생각해볼만함 > 이 상황이 왜 필요할까? > 낮이 된다면 부숴서 더 빨리 갈 수 있는 경우를 위해 > 이거밖에 없음
 - 매번 존버를 고려할 필요 없이, 낮과 밤에 대해서만 분리하고, 밤에만 존버를 한다를 추가해주면 됨
 - 다만, 생각 없이 급하게 문제를 풀려다 보니, 1트 와 같이 좀 정리가 안된 상태로 제출을 해서, 낮과 밤 정리가 잘 안되었을 것 같음
 - 깔끔하게 돌려서 통과할 수 있던 case

 - BFS 에서의 상황별 정리 > 최대한 깔끔하고 중복 없게 (하지만 이번 case 는 중복이 조금은 있는걸 감안한 문제임)
 - 3중 배열을 활요한 case 를 가지고 가는 것에 대한 생각 (BFS 역추적)
'''

I, J, K = map(int, input().split())
total_maze = [list(map(int, input().strip())) for _ in range(I)]  # 메이즈 어디로 갈지를 여기서 판단하면서 나아간다
status_maze = [[[0] * J for _ in range(I)] for _ in range(K + 1)]  # 상황 체크만 되면 되므로, 메이즈의 모습은 필요 없음
status_maze[0][0][0] = 1  # 방문을 함
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def pro1():
    global status_maze
    dq = deque()  # 내가 이번에 위치해서 볼 대상 > 현재 위치, 낮인지 밤인지, 몇 번 뽀갰는지에 대한 정보 포함
    dq.append(((0, 0), 1, True, 0))

    while dq:
        cur_position, times, is_day, break_cnt = dq.popleft()

        if cur_position == (I - 1, J - 1):
            return times

        if not is_day:  # 벽을 뽀갤 수 없고, 자기 자리에서 기다릴 수도 있음
            for k in range(4):
                mi = cur_position[0] + di[k]
                mj = cur_position[1] + dj[k]
                # 범위안에 든다, 벽이 아니다, 현재 부순 벽 갯수 상 visit 한적 없다
                if 0 <= mi < I and 0 <= mj < J and total_maze[mi][mj] == 0 and status_maze[break_cnt][mi][mj] == 0:
                    status_maze[break_cnt][mi][mj] = 1  # 여기는 visit 함
                    dq.append(((mi, mj), times + 1, not is_day, break_cnt))
            # 4번의 경우가 돌았을 경우, 현재 포지션을 유지할 수도 있다 (다음번에는 낮이기 때문에 제자리에 있을 수 없음)
            dq.append((cur_position, times + 1, not is_day, break_cnt))

        else:  # 벽을 뽀갤 수 있고, 기다릴 필요가 없음
            for k in range(4):
                mi = cur_position[0] + di[k]
                mj = cur_position[1] + dj[k]
                # 범위안에 든다
                if 0 <= mi < I and 0 <= mj < J:
                    if total_maze[mi][mj] == 0 and status_maze[break_cnt][mi][mj] == 0:  # 일반 길임
                        status_maze[break_cnt][mi][mj] = 1
                        dq.append(((mi, mj), times + 1, not is_day, break_cnt))

                    elif break_cnt < K and total_maze[mi][mj] == 1 and status_maze[break_cnt + 1][mi][
                        mj] == 0:  # 벽인데, 이 벽을 부순 상황을 겪지 않았다면
                        status_maze[break_cnt + 1][mi][mj] = 1
                        dq.append(((mi, mj), times + 1, not is_day, break_cnt + 1))
    return -1


def main():
    print(pro1())


main()
