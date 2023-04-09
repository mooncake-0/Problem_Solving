import sys

sys.stdin = open("input_19237.txt")
input = sys.stdin.readline

# N 공간 크기 <= 20 (MAP 은 만들어도 될 것으로 보임)
# M 상어 마리수 <= N^2
# k 냄새 제한시간 <= 1000
N, M, k = map(int, input().split())
pool = []
shark_valid = [0] * (M + 1)  # 존재 여부
shark_positions = [0] * (M + 1)  # 위치

for i in range(N):
    tmp = list(map(int, input().split()))  # 한 리스트
    status = []
    for j in range(len(tmp)):
        if tmp[j] != 0:  # 존재하는 상어
            shark_positions[tmp[j]] = (i, j)
            shark_valid[tmp[j]] = 1
            status.append([tmp[j], tmp[j], k])
        else:
            status.append([0, 0, 0])
    pool.append(status)

# 1 - 상 / 2 - 하 / 3 - 좌 / 4 - 우
dir_map = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
shark_dir = [0]
shark_dir += list(map(int, input().split()))  # 1번 ~ M번 상어 방향

# 상하좌우 (-1,0), (1,0), (0,-1), (0,1) 에 대하여
shark_dir_pri = [0]
for sidx in range(1, M + 1):  # 1번 ~ M번 상어까지에 대한 우선순위
    sidx_map = dict()
    for key in range(1, 5):
        sidx_map[key] = list(map(int, input().split()))
    shark_dir_pri.append(sidx_map)

time_elapsed = 0

''' 현재 상어가 갈 곳을 판단한다'''
def judge_position(s_idx, s_pos, s_dir):
    # print(s_idx, s_pos, s_dir)
    # 현재 방향에 따른 우선순위
    pri_directions = shark_dir_pri[s_idx][s_dir]  # 그 상어의 그 방향일 때의 우선순위 list
    # print(pri_directions)
    # 1,2,3,4 가 나온다
    while True:
        for dIdx in pri_directions:
            mi = s_pos[0] + dir_map[dIdx][0]
            mj = s_pos[1] + dir_map[dIdx][1]
            # print(mi, mj)
            if 0 <= mi < N and 0 <= mj < N and pool[mi][mj][0] == 0 and pool[mi][mj][1] == 0:
                return (mi, mj, dIdx)  # 갈 수 있는 빈 칸이다 (상어도 없고, 냄새도 없음)

        # 갈 수 있는 빈칸이 없었다면 우선 순위대로 내 냄새가 있는 곳을 판단한다
        for dIdx in pri_directions:
            mi = s_pos[0] + dir_map[dIdx][0]
            mj = s_pos[1] + dir_map[dIdx][1]
            if 0 <= mi < N and 0 <= mj < N and pool[mi][mj][1] == s_idx:
                return (mi, mj, dIdx)

exited = False
# 현재 pool 은 (존재상어, 상어의 냄새, 냄새 시간) 으로 기록되어있다.
while sum(shark_valid) > 1:
    if time_elapsed >= 1000:
        exited = True
        print(-1)
        break
    m_pos = [0] * (M + 1)
    # 각 상어를 움직인다
    for sidx in range(1, M + 1):
        if shark_valid[sidx] == 0:
            continue
        cur_shark_pos = shark_positions[sidx]  # 현재 상어의 위치
        cur_shar_dir = shark_dir[sidx]  # 현재 상어의 방향

        mi, mj, d_idx = judge_position(sidx, cur_shark_pos, cur_shar_dir)

        # 방향과 가게될 곳을 미리 저장해둔다
        if (mi, mj) not in m_pos:
            m_pos[sidx] = (mi, mj)
            shark_dir[sidx] = d_idx
        else:  # 중복되는 상어 존재 # 이미 있다는건 내가 더 큰 놈이란 소리, 이 상어는 제거된다
            pool[cur_shark_pos[0]][cur_shark_pos[1]][0] = 0
            shark_positions[sidx] = 0
            shark_valid[sidx] = 0

    for s_idx in range(1, M + 1):
        if shark_valid[s_idx] == 0:
            continue
        mi, mj = m_pos[s_idx]
        cur_shark_pos = shark_positions[s_idx]  # 현재 상어의 위치
        # m_pos 에 있는 애들
        # 움직인다 ( pos 변경, dir 변경, time 체킹하며 pool변경)
        pool[mi][mj] = [s_idx, s_idx, k + 1]  # 아래서 1씩 빠지기 때문에 미리 하나 더
        shark_positions[s_idx] = (mi, mj)

        # 있었던 곳의 상태 변경
        pool[cur_shark_pos[0]][cur_shark_pos[1]][0] = 0

    # 다 움직였으면 모든 곳을 일괄적으로 시간을 하나씩 뺀다
    for i in range(N):
        for j in range(N):
            if pool[i][j][2] != 0: # 0 이 아닌놈은 1 씩 빼주는데,
                if pool[i][j][2] == 1: # 그 중 하나 남은 놈들은
                    pool[i][j][1] = 0 # 상어 흔적도 없애준다
                pool[i][j][2] -= 1
    time_elapsed += 1
    # for x in pool:
    #     print(*x)
    # print("===================")
if not exited:
    print(time_elapsed)