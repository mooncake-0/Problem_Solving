import sys
from heapq import *

'''
포인트
 - 다익스트라 알고리즘의 흐름의 이해
 - 문제좀 똑바로 읽기;

'''

input = sys.stdin.readline

N, M, TG = map(int, input().split())

NODES = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    NODES[a].append((b, c))


def pro1(start):
    global each_times
    hq = []
    heappush(hq, (0, start))  # 가중치, NODE 로 넣는다. 그럼 가중치가 낮은것부터 탐색이 보장된다

    anw = [-2] + [-1] * (N)
    anw[start] = 0  # 현재 자신까지 오기위한 최단경로를 정의해줘야 한다

    while hq:

        distance_root_to_cur, cur_node = heappop(hq)

        # 이 앞에서 판단하는 경우가 더 작거나 같은 경우밖에 안들어옴.
        if distance_root_to_cur > anw[cur_node]:
            continue

        # 같은 경우는 이번에 판단해야할 경우
        # 작은 애가 먼저 앞쪽으로 들어오기 때문에, 가중치 (root 로부터 거리가 높은 애들은 자연스럽게 뒤로 간다)
        # 마지막에 판단할 필요가 없는 애들이 쫙 빠질 것으로 예상
        # anw[cur_node] 가 더 큰 경우는 들어올 수가 없다 :: 아래서 작은애로 최신화 해주고, 최신화된 애만 큐에 넣는거기 때문

        # 판단이 필요한 경우
        for dest_node, distance_cur_to_dest in NODES[cur_node]:
            # 판단이 된적이 없거나 or 이번에 탐색하는 경로가 현재 저장된 애보다 적을 때 얘로 적용
            if anw[dest_node] == -1 or distance_root_to_cur + distance_cur_to_dest < anw[dest_node]:
                anw[dest_node] = distance_root_to_cur + distance_cur_to_dest
                heappush(hq, (anw[dest_node], dest_node))

    # 일단 결과를 저장
    each_times.append(anw)


def main():
    global each_times

    each_times = [0] # 결과적으로 각 NODE 들의 모든 NODE 까지로의 최단거리 LIST 를 모두 저장한다 # 용량 문제 발생가능하긴 해보임 # 하지만 발생하지 않았군 후후
    # N = 1000 이므로 ㄱㅊ은 수준인듯
    # 용량 문제는 대부분 q 같은 곳에 무분별하게 양이 늘어날 때 발생하긴 함

    for i in range(1, N + 1):
        pro1(i)

    max_times = -1
    for i in range(1, N+1):
        # i > TG > i 로의 시간
        max_times = max(max_times, each_times[i][TG] + each_times[TG][i]) # 왕복 시간이 가장 큰 친구를 체크한다

    print(max_times)


main()
