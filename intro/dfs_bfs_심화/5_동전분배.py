import sys

sys.stdin = open("input_5.txt")

T = int(input())

def DFS(node):  # node = coin 리스트 index
    global min_value
    if node == N:
        temp = set()
        temp.add(sum(a))
        temp.add(sum(b))
        temp.add(sum(c))
        if len(temp) == 3:
            if min_value > max(temp) - min(temp):
                min_value = max(temp) - min(temp)
            return
    else:
        a.append(coins[node])
        DFS(node + 1)
        a.remove(coins[node])
        b.append(coins[node])
        DFS(node + 1)
        b.remove(coins[node])
        c.append(coins[node])
        DFS(node + 1)
        c.remove(coins[node])

for _ in range(T):
    N = int(input())
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    # print(coins, sum(coins))
    a = []
    b = []
    c = []
    min_value = 1000000000
    DFS(0)
    print(min_value)
