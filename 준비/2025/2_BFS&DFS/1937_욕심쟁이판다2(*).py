import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
bamboo = [list(map(int, input().split())) for _ in range(N)]

di, dj = [1, 0, -1, 0], [0, -1, 0, 1]

## 메모이제이션 느낌날 때 팁 -> 사실상 DP 문제였음
## 틀을 마련하라
## DP 느낌으로 따라가봐라!! 하나씩 하나씩! 이런 느낌 문제 더 풀어보고 싶다

# 1번에서 둘다 틀려서 새롭게 풀이
# my_largest_position 한 값을 가져와서, 계속 저장해 나가는 형태로 할 수는 없을까?
# 가령, a 가 my_largest_position 을 하면, 주위에 탐색할 친구들을 찾음
# 그럼 각 position 에서 my_largest_position 을 한다. (그 결과는 저장이다)
# 메모이제이션의 틀을 한번 Setting 해본게 중요했음. 그리고 꼭 DFS 라고 해서 순차적으로 탐색할 필요 없고, DFS 결과들을 모아서 판별시키는 느낌도 괜찮음!
def my_largest_path(cur_pos):
    global path_db

    # 뭔가 최신화가 안되어 있다?
    flag = True
    judge = []
    for k in range(4):  # 각 방향으로 갔을 때의 Largest_path 를 가져와본다 (그 중 max 를 판별해서 저장값으로 반환할 예정)
        mi = cur_pos[0] + di[k]
        mj = cur_pos[1] + dj[k]
        if 0 <= mi < N and 0 <= mj < N and bamboo[mi][mj] > bamboo[cur_pos[0]][cur_pos[1]]:
            flag = False
            if path_db[mi][mj] == -1:
                path_db[mi][mj] = my_largest_path((mi, mj))
            judge.append(path_db[mi][mj] + 1)

    if flag:  # 갈 곳이 없으면 무조건 1
        return 1

    return max(judge)


path_db = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if path_db[i][j] == -1:  # 아직 저장안된 경우만
            path_db[i][j] = my_largest_path((i, j))

max_val = path_db[0][0]
for i in range(N):
    for j in range(N):
        max_val = max(max_val, path_db[i][j])
print(max_val)

