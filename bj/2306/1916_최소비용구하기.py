import sys
from heapq import *

sys.stdin = open("input_1916.txt")
input = sys.stdin.readline

# N 개의 되시, M개의 버스
# A 번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화
# 도시번호 1 ~ N

N = int(input())
M = int(input())
bus_info = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    bus_info[a].append((b, c))


def pro1(s, tg):
    hq = []
    heappush(hq, (0, s))  # ROOT 에서 CUR_NODE 가중치 합, CUR_NODE # root 에서 시작

    anw_list = [-2] + [-1] * N  # -1 > 갈 수 없음
    anw_list[s] = 0

    while hq:

        dist_root_to_cur, cur_node = heappop(hq)

        ''' 같은 것을 내리기 위함 > 최신화는 되었을거고, 탐색 대상'''
        ''' dist_rtc 더 작은 것은 나올리가 없음 > 최신화를 미리 해주기 때문 '''
        ''' dist_rtc 더 큰 것은 pass 해도 좋음'''
        if dist_root_to_cur > anw_list[cur_node]:
            continue

        for choices in bus_info[cur_node]:
            dest_node = choices[0]
            dist_cur_to_dest = choices[1]

            # 처음 판단을 해야하거나, 최신화가 필요하다면
            if anw_list[dest_node] == -1 or dist_root_to_cur + dist_cur_to_dest < anw_list[dest_node]:
                anw_list[dest_node] = dist_root_to_cur + dist_cur_to_dest
                heappush(hq, (anw_list[dest_node], dest_node))

    print(anw_list[tg])

def main():
    s, tg = map(int, input().split())
    pro1(s, tg)


main()
