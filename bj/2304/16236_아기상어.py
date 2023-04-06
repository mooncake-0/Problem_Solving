import sys
from collections import deque

sys.stdin = open("input_16236.txt")
input = sys.stdin.readline

'''
포인트
 - 시뮬레이션 문제
 - 답이 계속 안나온다면 완벽하지 않은 것 같은 로직을 먼저 점검하는게 맞음. (이렇게 되겠지? 하는거 안됨)
 - N 이 크지 않으므로, 다양한 자료구조를 사용해봐도 된다는 생각
 - 다시 필요한 자료구조들, 소모성 있는 자료구조들에 대한 구분
 - 새롭게 해봤던 BFS 의 형태 

'''

# 위쪽으로, 위 다음엔 왼쪽으로 먼저 탐색한다
# 차피 점검하므로 상관 없음
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

N = int(input())


def judge_passable(position):
    global temp_path
    # 범위 안에 있다
    if position[0] < 0 or position[0] >= N:
        return False
    if position[1] < 0 or position[1] >= N:
        return False
    if room[position[0]][position[1]] > shark_size:
        return False
    if temp_path[position[0]][position[1]] < 0:
        return False
    return True


# 덱 안에 있는애들 뽑으면서 같은 거리인 애들 중, 우선권을 가지는 애들이 있는지 판단
# 차피 덱은 사라질거고, position 수가 많아봐야 400 이기 때문에 큰 부담 없을 것으로 보임
def judge_others(dq, cur_position, cur_elapsed_time):
    # 현재 덱에 있는건 searching 하는 모든 지점이기 때문에, room 수도 판단해줘야 함
    while dq:
        another_position, elapsed_time = dq.popleft()

        # elapsed Time 커지기 시작하면 끝임
        if elapsed_time > cur_elapsed_time:
            return cur_position
        # 물고기 있는 곳인지 판단
        in_room = room[another_position[0]][another_position[1]]

        if 0 < in_room < shark_size:  # 물고기가 있고, 상어가 먹을 수 있음
            # cur_position 보다 더 우선권을 가지는 친구라면, 이 친구로 대체해준다
            if cur_position[0] > another_position[0]:  # 새로운 녀석이 더 작으면 무조건 교체임
                cur_position = another_position
            elif cur_position[0] == another_position[0]:  # 같은 높이라면 j 값이 더 작으면 교체임
                if cur_position[1] > another_position[1]:
                    cur_position = another_position
            # 그 외면 그냥 유지한다
    return cur_position


def pro1():
    global temp_path, shark_size
    dq = deque()
    dq.append((shark_pos, 0))

    # 먹이를 먹을 때마다 다시 비워준다
    temp_path = [[0] * N for _ in range(N)]
    temp_path[shark_pos[0]][shark_pos[1]] = -1  # 시작 하는 곳도 지났음

    cur_eating = 0
    time = 0  # 먹을 경우 소모한 시간을 더해준다

    # 종료는 도착지가 있는게 아니고 무조건 갈 곳이 없으면 종료 된다
    while dq:

        cur_pos, cur_time_elapsed = dq.popleft()
        in_room = room[cur_pos[0]][cur_pos[1]]

        if in_room > 0:  # 물고기가 있고, 잡아먹을지 판단을 할 것이다 (사실 여기는 자기와 동일하거나, 낮은 애들만 들어옴)
            # 현재 사이즈 보다 작을 경우에만 먹먹 가능
            # 만난 순간 다른 애들이 있는지 덱에서 확인하는건 어떠한가?
            # 지금 거리 얘인 애를 조질건데, 혹시 덱에 같은 거리인 애중에 더 조질애 있냐? 라고 보면 될듯?
            if shark_size > in_room:  # 먹는다

                cur_pos = judge_others(dq, cur_pos, cur_time_elapsed)
                in_room = room[cur_pos[0]][cur_pos[1]]

                # 거리 초기화, time 더해주기
                # size 재계산
                cur_eating += 1

                if cur_eating == shark_size:  # 내가 먹은 수와 내 사이즈가 동일해질 때
                    shark_size += 1
                    cur_eating = 0

                time += cur_time_elapsed
                temp_path = [[0] * N for _ in range(N)]
                temp_path[cur_pos[0]][cur_pos[1]] = -1  # 이번 route 에서 내가 먹은곳은 끝
                room[cur_pos[0]][cur_pos[1]] = 0
                dq.clear()
                dq.append(((cur_pos[0], cur_pos[1]), 0))
                continue

        for k in range(4):
            mi = di[k] + cur_pos[0]
            mj = dj[k] + cur_pos[1]
            if judge_passable((mi, mj)):
                dq.append(((mi, mj), cur_time_elapsed + 1))
                temp_path[mi][mj] = -1

    print(time)


# 처음 아기상어의 크기는 2, 상하좌우로 1씩 움직인다
# 자신보다 크기가 큰 물고기는 먹을 수도, 지나갈 수도 없다
# 자신과 크기가 같은 물고기는 먹을 수 없지만 지나갈 수 있다.

# N*N 의 수조관을 만든다
shark_pos = ()
shark_size = 2
room = []

fishes_dict = dict()

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if l[j] == 9:
            shark_pos = (i, j)
    room.append(l)
room[shark_pos[0]][shark_pos[1]] = 0  # 위치만 알았으면 돌아다닐 수 있는 곳일 뿐임
pro1()
