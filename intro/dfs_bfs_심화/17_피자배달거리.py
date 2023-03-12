# 조합 DFS 를 사용해서 계속해서 최솟값을 찾고 선정하는 방식으로 품
import sys
from collections import deque

sys.stdin = open("input_17.txt")

T = int(input())


def find_length():
    # houses 를 돌리면서 pizza 집과의 거리를 찾는다.
    anw = 0
    for h in houses:
        pizz_distances = []
        for p in pizzas:
            if p in remove_chosen:
                continue
            distance = abs(p[0] - h[0]) + abs(p[1] - h[1])
            pizz_distances.append(distance)
        anw += min(pizz_distances)

    return anw


# remove_chosen 에 있는 녀석들을 제외하고
# pizzas 에 있는 녀석들을 대상으로


def dfs(chosen, index):  # pizzas array 안에 있는 녀석들 중 random 으로 중복-순서 없이
    if chosen == remove_needed:
        all_case_distances.append(find_length())
    else:
        for i in range(index, len(pizzas)):
            remove_chosen.append(pizzas[i])
            dfs(chosen + 1, i + 1)
            remove_chosen.remove(pizzas[i])


# 0 은 빈칸, 1은 집, 2는 피자집
for _ in range(T):
    N, survive = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]

    houses = []
    pizzas = []

    for i in range(N):
        for j in range(N):
            if town[i][j] == 1:
                houses.append((i, j))
            elif town[i][j] == 2:
                pizzas.append(((i, j)))

    remove_chosen = []
    remove_needed = len(pizzas) - survive
    # pizzas 에서 random 으로 survive 개를 고르는 Combination 을 완성한다

    all_case_distances = []
    dfs(0, 0)

    print(min(all_case_distances))
    # 그 때 각 집으로부터 가장 가까이에 있는 피자집 거리를 합해주는 로직을 작성하고, 이를 합해서 경우를 구한다
    # list 에 추가하여, 최솟값을 구한다 -> Least 일 때의