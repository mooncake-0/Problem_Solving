import sys
from collections import deque

'''
포인트
 - 설계는 잘 했음 > 원래 하던 방식이 DFS 였으니 DFS 로 할 일을 하고, 필요한 BFS들을 돌리는 생각으로 함
 - 시간 최적화는 자료구조로 하는 것. 어떤 자료구조를 어떻게 쓸지가 매우 중요
 - dict 을 평소와 반대로 써보는 생각이 좋았던 듯 (꽤 빠른 시간으로 진행됨)
 - 예제 만들기 > 극한을 만들만 하면 만들어봐라 (100*100 이라 만들만 했음) 
 - anw = 100 으로 세팅해놓은거가 문제였음 .. 
'''

sys.setrecursionlimit(100000)
sys.stdin = open("input_2146.txt")
input = sys.stdin.readline

N = int(input())
islands = [list(map(int, input().split())) for _ in range(N)]
edges = []
all_edges = dict()

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def DFS(position):
    global visited, tmp, idx

    visited[position[0]][position[1]] = 1

    for k in range(4):
        mi = position[0] + di[k]
        mj = position[1] + dj[k]
        if 0 <= mi < N and 0 <= mj < N:
            if visited[mi][mj] == 0 and islands[mi][mj] == 1:
                DFS((mi, mj))
            elif visited[mi][mj] == 0 and islands[mi][mj] == 0:  # 밖으로 나가지는 부분
                tmp.append((mi, mj))
                if (mi, mj) in all_edges:
                    all_edges[(mi, mj)].add(idx)
                else:
                    real_tmp = set()
                    real_tmp.add(idx)
                    all_edges[(mi, mj)] = real_tmp


def main():
    global tmp, visited, idx
    # 일단 돌면서 모든 섬의 경계 Line 을 파악해야한다
    visited = [[0] * N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if islands[i][j] == 1 and visited[i][j] == 0:  # 섬이 있지만 안간곳
                tmp = []
                DFS((i, j))
                idx += 1
                edges.append(tmp)

    anw = 100000

    #  나온 애들을 데리고 BFS를 돌려야 한다
    # 1번 SET > 나머지 SET에 존재하는 애들인지를 판단하면서 distance 를 판단
    for i in range(len(edges) - 1):  # 마지막 섬은 안해도 된다

        dq = deque()

        for item in list(edges[i]):
            dq.append((item, 1))

        # 이미 그 포지션에 있는 애를 지나간다면, 무조건 먼저 지나간 애가 더 짧을 것이기 때문에, 중복해서 지나갈 필요가 없음
        path_visited = set()

        while dq:

            cur_path, times = dq.popleft()

            # all_edges 안에 있음
            if cur_path in all_edges:  # 있다면 판별 들어가는 것
                # 나만 있을 경우 > 걸러야 함
                if len(all_edges[cur_path]) == 1:
                    if i in all_edges[cur_path]:  # 나만 있는 경우
                        pass
                    else:  # 다른 애만 있는 경우 (도달한 것
                        # print(cur_path, times)
                        anw = min(times, anw)
                        break

                else:
                    if i in all_edges[cur_path]:  # 나랑 다른애 만 있음
                        # print(cur_path, times)
                        anw = min(1, anw)
                        break
                    else:  # 다른 애 둘이 겹치게 되는 부분 그냥대로 속행
                        # print(cur_path, times)
                        anw = min(times, anw)
                        break

            for k in range(4):
                mi = cur_path[0] + di[k]
                mj = cur_path[1] + dj[k]
                if 0 <= mi < N and 0 <= mj < N and (mi, mj) not in path_visited:
                    path_visited.add((mi, mj))
                    dq.append(((mi, mj), times + 1))
    print(anw)


main()
