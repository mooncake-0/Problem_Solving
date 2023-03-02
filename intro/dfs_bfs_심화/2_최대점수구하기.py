import sys

sys.stdin = open("input_1.txt")


def DFS(node, score_sum, time_sum):
    global score_max
    if time_sum > M:
        return
    if node == N:
        if score_sum > score_max:
            score_max = score_sum
        return
    else:
        DFS(node + 1, score_sum + score_time[node][0], time_sum + score_time[node][1])
        DFS(node + 1, score_sum, time_sum)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 합이 20 이 되는 부분 집합 묶음을 찾아서, 가장 높은 점수를 출력
    score_time = []
    for _ in range(N):
        score_time.append(list(map(int, input().split())))
    score_max = 0
    DFS(0, 0, 0)
    print(score_max)
