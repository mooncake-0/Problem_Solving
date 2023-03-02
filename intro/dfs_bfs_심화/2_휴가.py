import sys

sys.stdin = open("input_2.txt")
# sys.stdin = open("temp.txt")

T = int(input())


def DFS(node, remaining):  # node 는 일차
    global is_working

    if remaining == 0:
        is_working = False

    if node == N + 1:
        last_cancel = False
        if remaining != 0:
            # 마지막 일은 못하는걸로 간주, pay 계산에서 뺀다
            last_cancel = True
        pay_sum = 0
        for i in range(len(worked)):  # index 들이 들어 있음
            if last_cancel and i == len(worked) - 1:
                break
            else:
                pay_sum += pays[worked[i]]
        pay_sums.append(pay_sum)
        return
    else:
        if is_working:
            # 다음으로 보낸다
            DFS(node + 1, remaining - 1)
        else:
            # 이 일차를 일하는 경우
            worked.append(node - 1)
            is_working = True
            DFS(node + 1, days[node - 1] - 1)
            # 이 일차를 하지 않는 경우
            worked.remove(node - 1)
            is_working = False
            DFS(node + 1, remaining)


for _ in range(T):
    # N 일까지 벌 수 있는 최대 금액
    N = int(input())
    days = []
    pays = []
    for _ in range(N):
        d, p = map(int, input().split())
        days.append(d)
        pays.append(p)
    # index 가 node-1
    is_working = False
    worked = []
    pay_sums = []
    DFS(1, 0)
    print(max(pay_sums))
