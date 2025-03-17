import sys

input = sys.stdin.readline

N = int(input())
bamboo = [list(map(int, input().split())) for _ in range(N)]

'''
시간을 절약할 수 있는 방법
- 이미 탐색한 곳은 탐색하지 말도록 하자
- visited 표시를 해서 다시 DFS 를 돌 필요 없게끔 만들 수 있다
- 탐색 결과 현재 max 값보다 크다면 최신화, 작다면 걍 표식만 하고 버림
'''

di, dj = [1, 0, -1, 0], [0, -1, 0, 1]
'''
### SOL 1 - 나쁘진 않은데,DFS 에 타는게 너무 많아서 시간 초과가 나긴 한다
# 깊은 생각 후에..
# 이미 Path 로 등재되어서 대소를 판별받은 경로 set 은 (크기로 결정 났든 안났든 상관 없음)
# 시작하는 조건에서 제외될 수 있음!! 하지만 DFS 를 도는 조건에서는 제외되면 안된다가 내 결론!!
def dfs(cur_pos, cur_path):
    global tmp_max_path
    judge = True
    for k in range(4):
        mi = cur_pos[0] + di[k]
        mj = cur_pos[1] + dj[k]
        if 0 <= mi < N and 0 <= mj < N and bamboo[cur_pos[0]][cur_pos[1]] < bamboo[mi][mj]:
            judge = False # 이번 Loop 는 판별할 조건이 아님
            start_remove[mi][mj] = 1  # 시작하는 조건에서 제외될 수 있다
            dfs((mi, mj), cur_path + 1)
    # 더이상 돌 곳이 없는 경우 이쪽으로 온다
    if judge:
        tmp_max_path = max(tmp_max_path, cur_path)

total_max_path = -1
start_remove = [[0] * N for _ in range(N)]  # DFS 트리거 제외될 수 있는 대상
for i in range(N):
    for j in range(N):
        if start_remove[i][j] == 0:  # 시작시 제외되어도 된다면
            tmp_max_path = -1
            dfs((i, j), 1)
            total_max_path = max(total_max_path, tmp_max_path)
print(total_max_path)
'''


## SOL2 - "자신의 위치에서 경로에 최대값을 항상 저장해두면?"

# dfs 를 돌리거나, 주변에 저장된 값이 있다면 +1 을 더해서 비교군에 넣는다
def my_largest_path(cur_position, this_path, this_visited):
    global max_val

    flag = True
    for k in range(4):
        mi = cur_position[0] + di[k]
        mj = cur_position[1] + dj[k]
        if 0 <= mi < N and 0 <= mj < N and bamboo[mi][mj] > bamboo[cur_position[0]][cur_position[1]] and (mi, mj) not in this_visited:
            if path_db[mi][mj] != -1:  # 다음 경로에 갈 녀석이 저장되어 있다면 "해당 경로로 갈 시" 나의 값을 내린다
                flag = False # for loop 이 도는동안 종료가 되어야 하기 때문에 여기서 처리
                this_path += path_db[mi][mj]  ## 저장되어 있으면 더이상 판단을 안해도 된다
                max_val = max(this_path, max_val)
                this_path -= path_db[mi][mj] # 그대로 다른 for 을 돌리기 때문에 빼줘야 한다

            else:  # 다음 경로에 갈 녀석이 저장되어 있지 않다면 dfs 에 넣는다
                flag = False # 이번 DFS 는 종료시점이 아님을 명시
                this_visited.add((mi, mj))
                my_largest_path((mi, mj), this_path + 1, this_visited)
                this_visited.remove((mi, mj))

    # DFS 가 종료되는 시점에만 여기로 온다
    if flag:  # 이번 path 는 종료한다
        max_val = max(this_path, max_val)
        # 종료 구간의 역할 - 무조건 1이 된다
        path_db[cur_position[0]][cur_position[1]] = 1

path_db = [[-1] * N for _ in range(N)]  # -1 은 아직 저장되지 않음
total_max_path = -1
for i in range(N):
    for j in range(N):
        max_val = -1
        this_visited = set()
        this_visited.add((i, j))
        my_largest_path((i, j), 1, this_visited)  # 그냥 쭉 돈다. path_db 와 함께 my_largest_path 에서 계산을 해낸다
        path_db[i][j] = max_val
        total_max_path = max(max_val, total_max_path)

for x in path_db:
    print(x)

print(total_max_path)