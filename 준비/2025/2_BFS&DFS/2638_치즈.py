import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

'''
용량, 시간 모두 Best 솔루션들 대비 많이 쓰긴 한 듯
하지만 해당 풀이가 나의 첫 풀이
'''


'''
첫 지점에 있는 점을 기준으로 DFS 를 시작 (무조건 0 이 보장이기 때문) - 바깥 영역을 정의
- 바깥에 있는 영역이 아니면 모두 치즈 안에 있는 0이다!! (연결이 안되어 있기 때문)
- 태초에 바깥에 있는 모든 점들을 보관하는 DFS 를 돌린다 - 녹은 점들을
- 그 점들에 매번 DFS 를 돌리긴 해야할 듯 하다

- 그 이후 이번 년도의 바깥영역이 준비되면
- array 를 돌면서 1인 부분을 찾아 C 를 판별한다
- C를 판별하면 각 global_map 에서 삭제된다

- 종료 판단 : DFS 를 막기는 어려울 듯
- 차라리 DFS 는 돌리고  N*N 한번 도는데 O(10000) 뿐이 안되니까, 1이 없을때를 보자
- 1이 없으면 모두 녹음, year 계산 완료
 '''

N, M = map(int, input().split())
cheese_map = [list(map(int, input().split())) for _ in range(N)]
outside = set()

di, dj = [1, 0, -1, 0], [0, -1, 0, 1]


def dfs(cur_pos):
    global outside

    for k in range(4):
        mi = cur_pos[0] + di[k]
        mj = cur_pos[1] + dj[k]
        if 0 <= mi < N and 0 <= mj < M and (mi, mj) not in outside and cheese_map[mi][mj] == 0:
            outside.add((mi, mj))
            dfs((mi, mj))


def amiMelting(cur_pos):
    cnt_outside = 0
    for idx in range(4):
        mi = cur_pos[0] + di[idx]
        mj = cur_pos[1] + dj[idx]
        if 0 <= mi < N and 0 <= mj < M and (mi, mj) in outside and cheese_map[mi][mj] == 0:
            # C 도 아니고 1 도 아닌 0, 그리고 외부 영역이여야 함
            cnt_outside += 1
    if cnt_outside >= 2:
        return True
    return False


anw = 0

while True:
    outside.add((0, 0))
    dfs((0, 0))  # 바깥 영역을 정의
    all_melted = True
    # 하나씩 돌면서 C 인 영역을 판단
    for i in range(N):
        for j in range(M):
            if cheese_map[i][j] == 1:
                all_melted = False  # 아직 치즈가 존재함
                if amiMelting((i, j)):  # 올해 녹을 놈인지 판단한다
                    cheese_map[i][j] = 'C'  # 녹을거라는 표시

    # print("--------------")
    # for a in cheese_map:
    #     print(a)

    if all_melted:
        break

    for i in range(N):
        for j in range(M):
            if cheese_map[i][j] == 'C':
                cheese_map[i][j] = 0

    anw += 1  # 올해 해결 못 했으니 한해가 지난다
    outside.clear()
    # print("year passed: ", anw)
    # for a in cheese_map:
    #     print(a)

print(anw)
