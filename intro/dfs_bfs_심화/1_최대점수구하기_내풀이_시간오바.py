import sys

sys.stdin = open("input_1.txt")


def DFS(node, time_sum):
    if time_sum >= M:
        if time_sum == M:
            score_sum = 0
            for i in used:
                score_sum += score_time[i][0]
            scores.append(score_sum)
        return
    else:
        for i in range(len(score_time)):
            if i not in used:
                used.append(i)
                time_sum += score_time[i][1]
                DFS(node + 1, time_sum)
                used.remove(i)
                time_sum -= score_time[i][1]


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 합이 20 이 되는 부분 집합 묶음을 찾아서, 가장 높은 점수를 출력
    score_time = []
    total = 0
    for _ in range(N):
        a = list(map(int, input().split()))
        total += a[1]
        score_time.append(a)
    scores = []
    used = []
    DFS(1, 0)
    print(max(scores))
