import sys
from collections import deque

'''
start 10:20
end 10:50

- 실수..가 있었으.. 
- 생각 나는 방향 > 시간 복잡도 생각 > 브루트 포스 맞다 판단하면 바로 ㄱ
- 시간복잡도 생각시 이건 아니다 싶으면 다른 방향으로 가야 하는 것
'''

sys.stdin = open("input_14502.txt")
input = sys.stdin.readline

# 64C3 .. 브루트 포스 돌리는거임
I, J = map(int, input().split())
LAB = [list(map(int, input().split())) for _ in range(I)]
empties = []
virus_pos = []

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
cnt_safety = 0
for i in range(I):
    for j in range(J):
        if LAB[i][j] == 0:
            cnt_safety += 1
            empties.append((i, j))
        if LAB[i][j] == 2:
            virus_pos.append((i, j))


def find_combination(choose, idx):
    global combinations
    if len(choose) == 3:
        combinations.append(choose[:])
    else:
        for i in range(idx, len(empties)):  # 0 인 녀석들 중에 고른다 (idx 를 고른다)
            choose.append(i)
            find_combination(choose, i + 1)
            choose.pop()


def run_viruses():
    viruses = deque()
    exists = set()
    plagued = 0

    # 초기 세팅
    for x in virus_pos:
        viruses.append(x)
        exists.add(x)

    while viruses:

        v_pos = viruses.popleft()

        for k in range(4):
            mi = v_pos[0] + di[k]
            mj = v_pos[1] + dj[k]
            if 0 <= mi < I and 0 <= mj < J and LAB[mi][mj] == 0 and (mi, mj) not in exists:
                viruses.append((mi, mj))
                exists.add((mi, mj))
                plagued += 1

    # 안전 지역의 갯수
    return cnt_safety -3 - plagued



def main():
    global combinations, LAB
    # empties 중에 combination 을 만든다
    combinations = []
    find_combination([], 0)
    max_val = -1
    for comb in combinations:  # LAB 을 바꿔줬다가, 돌리고 난 다음에는 다시 바꿔줌
        for wall_pos_idxes in comb:
            LAB[empties[wall_pos_idxes][0]][empties[wall_pos_idxes][1]] = 1
        max_val = max(max_val, run_viruses())
        for wall_pos_idxes in comb:
            LAB[empties[wall_pos_idxes][0]][empties[wall_pos_idxes][1]] = 0

    print(max_val)

main()
