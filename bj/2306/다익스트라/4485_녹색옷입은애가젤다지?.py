import sys
from heapq import *
'''
포인트
 - BFS 로 돌려도 풀리긴 한다고 한다 (다만, HQ 를 좀 활용해야 하는듯?) 
 - 다만, 최적 경로이므로 다익스트라에 대한 생각을 해볼 수도 있는 듯 하다 
 - "다익스트라에서 정점이란 무엇인가?" 를 좀 더 생각해볼 수 있는 듯. dict 을 활용하는 것도 좋았음 
'''
sys.stdin = open("input_4485.txt")
input = sys.stdin.readline

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


# [0][0] >> [N-1][N-1]
def dijkstra(N):
    global NODES

    hq = []
    heappush(hq, (NODES[0][0], (0, 0)))  # (가중치, NODE 이름) 으로 간다

    anw_dict = dict()
    anw_dict[(0, 0)] = NODES[0][0]  # 현재까지 저장된 최단 경로를 저장한다

    while hq:

        distance_root_to_cur, cur_node = heappop(hq)

        if distance_root_to_cur > anw_dict[cur_node]:  # 더 큰 값이 들어올 경우 지나친다 (없을 경우는 들어오지 않을 것)
            continue

        # cur_node 에서 갈 수 있는 곳들을 말해준다
        for k in range(4):
            dest_node_i = cur_node[0] + di[k]
            dest_node_j = cur_node[1] + dj[k]

            if 0<= dest_node_i < N and 0<= dest_node_j < N:

                dest_val = NODES[dest_node_i][dest_node_j]

                if (dest_node_i, dest_node_j) not in anw_dict or distance_root_to_cur + dest_val < anw_dict[(dest_node_i, dest_node_j)]:
                    anw_dict[(dest_node_i, dest_node_j)] = distance_root_to_cur + dest_val
                    heappush(hq, (anw_dict[(dest_node_i, dest_node_j)], (dest_node_i, dest_node_j)))

    return anw_dict[(N-1, N-1)]

def main():
    global NODES

    problem_num = 1
    ''' each TC'''
    while True:

        N = int(input())

        '''finish program'''
        if N == 0:
            break

        ''' execute TC'''
        NODES = [list(map(int, input().split())) for _ in range(N)]
        anw = dijkstra(N)

        print("Problem " + str(problem_num) + ": " + str(anw))
        problem_num += 1


main()
