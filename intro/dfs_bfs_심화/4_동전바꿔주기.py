import sys
import time
sys.stdin = open("input_4.txt")


def DFS(node, cur_price):
    global ways
    if cur_price >= paper:
        if cur_price == paper:
            ways += 1
        return
    if node > N - 1:
        if cur_price == paper:
            ways += 1
        # print("evaluate: ", cur_price, ways)
        return
    else:
        # 리스트 내 인덱스 = node -1
        for cnt in range(0, coins_cnt[node][1] + 1):
            # cnt 개를 써서 다음으로 보낼 거임
            # print(node, ",", cnt, "::", cur_price)
            cur_price += cnt * coins_cnt[node][0]
            DFS(node + 1, cur_price)
            cur_price -= cnt * coins_cnt[node][0]
            # print("2nd: ", node, ",", cnt, "::", cur_price)

T = int(input())

start = time.time()

for _ in range(T):

    paper = int(input())
    N = int(input())
    coins_cnt = []
    for i in range(N):
        coins_cnt.append(list(map(int, input().split())))
    # 코인들로 paper 를 거슬러줄 방법 (쓰냐 안쓰냐 ㄲ)
    # Node = 코인 고르는 인덱스 (각 코인 모두 할거임)
    ways = 0
    DFS(0, 0)
    print(ways)
    print("time :", time.time() - start)
