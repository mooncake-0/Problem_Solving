import sys

sys.setrecursionlimit(100000)
sys.stdin = open("input_2573.txt")
input = sys.stdin.readline


di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def print_iceberg(cur_pos):
    print(cur_pos)
    for x in icebergs:
        print(x)
    print("==============================")


# 주변에 0 이 있는 갯수만큼 - 당함
# 두 덩어리가 될 때 종료. 덩어리 판단 필요? 근데 계속 돌리긴 어려운데... 90,000 을 100번만 돌려도
def dfs(position, checked):
    global I, J, icebergs

    # print_iceberg(position)
    # 현재 포지션에 대해서 수정을 해준다
    checked[position[0]][position[1]] = 1

    # 다음날을 위해 빙하를 녹여준다
    # 가장자리들은 모두 0임을 보장해줌
    cnt = 0
    for k in range(4):
        mi = position[0] + di[k]
        mj = position[1] + dj[k]
        if icebergs[mi][mj] == 0 and checked[mi][mj] == 0:
            cnt += 1

    # 다음날 빙하 세팅
    if icebergs[position[0]][position[1]] < cnt:
        icebergs[position[0]][position[1]] = 0
    else:
        icebergs[position[0]][position[1]] -= cnt

    # 이제 checked 확인
    for k in range(4):
        mi = position[0] + di[k]
        mj = position[1] + dj[k]
        if icebergs[mi][mj] != 0 and checked[mi][mj] != 1:
            dfs((mi, mj), checked)


def main():
    global I, J, icebergs
    I, J = map(int, input().split())  # 3 ~ 300 // 90,000
    icebergs = [list(map(int, input().split())) for _ in range(I)]
    days = 0

    while True:

        # 돌리기 전에 매번 바뀌는 것들을 설정해 놓는다
        checked = [[0] * J for _ in range(I)]
        cnt = 0
        for i in range(I):
            for j in range(J):
                if icebergs[i][j] != 0 and checked[i][j] != 1:  # iceberg 가 있으나, checked 가 0이여야 dfs를 돌린다
                    # DFS
                    cnt += 1
                    dfs((i, j), checked)
        # print_iceberg((0,0))
        # print("==  ==  == = =  = = = = = == = = = = = ==  = = = =  =  = = = = = = = = = = =")
        # 다 돌고 난 뒤에 확인해본다
        # 확인해본 결과 = 현재 days
        # 다 돌린 결과 = days + 1
        if cnt >= 2:  # 두 덩어리 이상
            print(days)
            return
        elif cnt == 0:  # 다 녹음
            print(0)
            return

        days += 1  # 다음으로 보낸 결과는 하루가 지난 결과임 (마지막에 더해줘야함)


main()
