import sys
from heapq import *

sys.stdin = open("input_5972.txt")
input = sys.stdin.readline


station, path = map(int, input().split())  # station : 정점 갯수
NODE_MAPS = [[] for _ in range(station + 1)]

for _ in range(path):
    s, e, w = map(int, input().split())
    NODE_MAPS[s].append((e, w))
    NODE_MAPS[e].append((s, w))


def pro1(TG, anw_list):
    hq = []
    heappush(hq, (0, TG))  # (TG 노드에서 현재 노드까지의 판단 거리값, 현재 노드)
    anw_list[TG] = 0

    while hq:
        distance_root_to_cur, cur_node = heappop(hq)  # 판단해볼 대상

        # cur_node 까지를 판단해보고 있음
        # cur_node 까지의 판단해보고자 하는 거리가 저장된 거리보다 크면 판단할 필요 없음.
        # 같으면 현재 그 위치에 대한 파악을 해야하므로 내려간다
        if anw_list[cur_node] < distance_root_to_cur:
            continue

        # 해당 노드는 판단 대상이 되었고, 연결된 애들을 살펴보자
        for linked_node, distance_cur_to_linked in NODE_MAPS[cur_node]:
            # 연결된 애까지의 갈 거리가 최신화가 필요하다면
            if anw_list[linked_node] == -1 or anw_list[linked_node] > distance_root_to_cur + distance_cur_to_linked:
                anw_list[linked_node] = distance_cur_to_linked + distance_root_to_cur
                heappush(hq, (anw_list[linked_node], linked_node))

    print(anw_list[len(anw_list) - 1])


def main():
    TG = 1  # 1번 NODE의 모든 정점까지의 최소 경로를 확보한다
    anw_list = [-2] + [-1] * (station)
    pro1(TG, anw_list)


main()
