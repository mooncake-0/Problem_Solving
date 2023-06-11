import sys

sys.setrecursionlimit(10000)

sys.stdin = open("input_5972.txt")
input = sys.stdin.readline

'''
이중배열로 선언했다가
메모리 초과 남 > NODE 수가 5만개인걸 고려했을때, 당연한 결과
DICT 활용으로 바꿔줌 > 시간 초과 남 > DFS 로 풀었을 때
> 가중치에 대한 최적화는 다익스트라 활용 필요

'''


station, path = map(int, input().split())
# station 이 정점 (1~50,000) >> DFS 는 오만제곱..? 2,500,000,000
# path 는 station 간 길 (1~50,000)
# path 에는 0 ~ 1,000 마리의 소가 있음
# 1 --> N 까지 가는중 최소한의 소를 마주하면서 갈 때, 그 떄 소 마리 수를 구하여라
# input 은 시작점 > 도착점 : 가중치


# 연결에 대한 이차원 배열을 제시
# map 으로 해놔야할듯
node_dict = dict()

# node_map = [[-1] * (station + 1) for _ in range(station + 1)]

# 각 배열에 가중치를 제시
for _ in range(path):
    s, e, w = map(int, input().split())
    node_dict[(s, e)] = w
    node_dict[(e, s)] = w
    # node_map[s][e] = w
    # node_map[e][s] = w  # 이건 필요할까?


# 일단 기본적으로 내가 갈 수 있는 모든 경로를 뿌리고, 최소 비용을 구하면 될 것 같긴한데?
# 1에선 > 2, 4 갈 수 있음
#       > 2 에선 > 1, 3, 4 갈 수 있음 (방문 node 1 제외)
#       > 4 에선 > 1,2,3 갈 수 있음 (방문 node 1제외)


# 일단 NAIVE 하게 가야한다
# 유일하게 생각나는게 DFS 하나인듯
def dfs(node, weight_sum):
    global visited, anw
    if node == station:
        # print(visited, " ", weight_sum)
        anw = min(anw, weight_sum)
        return
    # 현재 node 에서 갈 수 있는 곳으로 간다
    else:
        for i in range(1, station + 1):

            # if node_map[node][i] != -1 and visited[i] != 1:  # 하지만, 지나온 것에 대해 체크를 해야한
            if (node, i) in node_dict and visited[i] != 1:
                visited[i] = 1
                # dfs(i, weight_sum + node_map[node][i])
                dfs(i, weight_sum + node_dict[(node, i)])
                visited[i] = 0


def pro1():
    global visited, anw
    # 1 >> station 까지 갈거임 (station = 갯수)
    visited = [0] * (station + 1)
    anw = 1000 * path
    visited[1] = 1
    dfs(1, 0)
    print(anw)


def main():
    pro1()


main()
