import sys

sys.stdin = open("input_2667.txt")
input = sys.stdin.readline
N = int(input())
towns = [list(map(str, input().strip())) for _ in range(N)]

di, dj = [0, 1, 0, -1],[1, 0, -1, 0]


def dfs(position):
    global towns, this_town_cnt

    towns[position[0]][position[1]] = "0"
    this_town_cnt +=1

    for i in range(4):
        mi = di[i] + position[0]
        mj = dj[i] + position[1]
        if 0<= mi < N and 0 <= mj < N and towns[mi][mj] == "1": # town cnt 가능시
            dfs((mi,mj))

def main():
    global town_cnts, this_town_cnt
    town_cnts = []
    for i in range(N):
        for j in range(N):
            if towns[i][j] == '1':
                this_town_cnt = 0
                dfs((i, j))
                town_cnts.append(this_town_cnt)
    town_cnts.sort()
    print(len(town_cnts))
    for x in town_cnts:
        print(x)

main()
