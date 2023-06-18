import sys
from heapq import *

'''
포인트
- 정점과 가중치를 어떻게 설계해야하는지에 대해 더 이해해볼 수 있음
- 당황스러운 느낌을 좀 넘으면 ㄱㅊ았음
'''
sys.stdin = open("input_10473.txt")
input = sys.stdin.readline

START_X, START_Y = map(float, input().split())
TG_X, TG_Y = map(float, input().split())
CANNON_CNT = int(input())
CANNON_POS = [(START_X, START_Y)] + [tuple(map(float, input().split())) for _ in range(CANNON_CNT)] + [(TG_X, TG_Y)]


# 두 지점 사이의 거리, 둘째자리까지
# 둘째짜리까지 했을 때 정확성이 살짝 떨어져서, 4까지 내려서 계산해본다
def findDistance(pos1, pos2):
    return round(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** (1 / 2), 4)


# 시간 소요는
# 0에서 출발하는건 무조건 걸어가는거임
# 그 외에는 모두 대포로 가는거임
def findTime(isWalking, distance):
    if isWalking:  # 시속 5m/s
        return round(distance / 5, 4)
    else:
        time = round(abs(distance - 50) / 5, 4)
        return time + 2

# CANNON POS 들을 정점으로 가질 때, 서로간의 대포 + 걷는 거리만큼의 이동시간을 가중치로 가지게 된다
# 0번이 시작 NODE, 마지막 번호가 TG NODE
NODES = [[-1] * (CANNON_CNT + 2) for _ in range(CANNON_CNT + 2)]

for i in range(CANNON_CNT + 2):
    for j in range(CANNON_CNT + 2):
        if i == j:
            NODES[i][j] = 0
        elif i < j:
            distance_between = findDistance(CANNON_POS[i], CANNON_POS[j])
            if i == 0:
                NODES[i][j] = findTime(True, distance_between)
            else:
                NODES[i][j] = findTime(False, distance_between)
        else:
            NODES[i][j] = NODES[j][i]

# NODES 완성, 이제 Dijkstra 하면 됨
def dijkstra(N):
    # 0번 NODE 시작, N-1 NODE 목표
    hq = []
    heappush(hq, (0, 0)) #root 에서 CUR_NODE 까지의 가중치 합, CUR_NODE

    anw_list = [-1] * N
    anw_list[0] = 0 # 첫 NODE 는 무조건 0의 가중치

    while hq:

        distance_root_to_cur, cur_node = heappop(hq)

        if distance_root_to_cur > anw_list[cur_node]:
            continue

        for idx in range(N):
            dest_node = idx
            distance_cur_to_dest = NODES[cur_node][idx]
            # 초기화되지 않은 경로이거나, 현재보다 더 짧은 경로를 찾았을 경우
            if anw_list[dest_node]== -1 or distance_root_to_cur + distance_cur_to_dest < anw_list[dest_node]:
                anw_list[dest_node] = distance_cur_to_dest + distance_root_to_cur
                heappush(hq, (anw_list[dest_node], dest_node))

    print(anw_list[N-1])


dijkstra(CANNON_CNT + 2)
