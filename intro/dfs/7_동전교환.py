import sys

sys.stdin = open("input_7.txt")


def DFS(node, cur_sum):
    # 만약 현재 진행되고 있는 카운트가, 이미 지금까지 최솟값을 넘어섰다면 그만 세도 됨
    if coin_cnt:
        if min(coin_cnt) < node:
            return

    if cur_sum >= change:
        if cur_sum == change:
            node -= 1  # 이번 횟수는 추가 횟수가 아니므로
            coin_cnt.append(node)  # 몇개째 선택한건지 coin_cnt 에 제출
    else:
        for x in coins:
            cur_sum += x
            DFS(node + 1, cur_sum)
            cur_sum -= x


T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    coins = list(reversed(coins))
    change = int(input())
    # 가장 적은 동전을 사용하여 거슬러줘라
    # 선택이 node, 몇 번 선택하든 change 가 안되면 다시 선택해야함
    coin_cnt = []
    DFS(1, 0)
    print(min(coin_cnt))
