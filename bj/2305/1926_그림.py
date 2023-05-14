import sys

sys.stdin = open("input_1926.txt")
input = sys.stdin.readline

'''
포인트
    - DFS 에서 함부로 중간에 return 하면 안됨. 종료조건을 명시해주는 것이기도 하기 때문
    - BFS 가 좀 더 좋았을 듯
    - pypy3 로 하면 메모리 초과남. python3 로 하면 통과 
'''

# I, J <= 500
# 500 * 500 = 250,000 (ㄱㅊ)
I, J = map(int, input().split())
pic_map = [list(map(int, input().split())) for _ in range(I)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def judge_possible(next_pos):
    if next_pos[0] < 0 or next_pos[0] >= I:
        return False
    if next_pos[1] < 0 or next_pos[1] >= J:
        return False
    if pic_map[next_pos[0]][next_pos[1]] != 1:
        return False
    return True


def DFS(cur_pos, area_cnt):
    global pic_map

    # 현재 포지션을 중심으로 주변에 움직일 곳이 있는지 판단.
    # 있다면 그 쪽으로 움직인다
    for i in range(4):
        mi = cur_pos[0] + di[i]
        mj = cur_pos[1] + dj[i]
        # 다음 (mi,mj)
        if judge_possible((mi, mj)):
            # 그 쪽으로 이동한다 = 거기를 먹는다
            pic_map[mi][mj] = 0
            area_cnt = DFS((mi, mj), area_cnt + 1)

    return area_cnt


# DFS 풀이
def pro1():
    global pic_map
    cnt = 0
    max_area = -1
    for i in range(I):
        for j in range(J):
            if pic_map[i][j] == 1:  # DFS 를 먹인다 (묶음이 있다는 뜻)
                cnt += 1
                pic_map[i][j] = 0  # 여기를 먹고 시작한다
                tmp = DFS((i, j), 1)
                max_area = max(max_area, tmp)

    # 한번도 DFS 를 돌지 않았다면 = 그림이 없다면
    if cnt == 0:
        max_area = 0
    print(cnt)
    print(max_area)


def main():
    pro1()


main()
