NODE_CNT = 6
NODE_MAP = [  # 가중치가 0 인 상황은 없다라는 가정 하에 다음과 같이 설계
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 5, 1, 0, 0],
    [0, 2, 0, 3, 2, 0, 0],
    [0, 5, 3, 0, 3, 1, 5],
    [0, 1, 2, 3, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 2],
    [0, 0, 0, 5, 0, 2, 0]
]


# 과제
# 1번 > 일반 다익스트라를 구현해보아라
# 선형탐색, WHILE 내부 for 문 > N^2
def pro1(TG):  # TG 입장에서 구할 것임

    min_paths = [-1] * (NODE_CNT + 1)  # 내가 구하고자 하는 것 (1번 입장에서 각 정점 별로의 최소 가중치 = 다른 입장에서 구하려면 새롭게 필요)
    visited = [0] * (NODE_CNT + 1)  # 위 list 와 동일하게 한 입장에서 구할 때 필요함.

    for i in range(1, NODE_CNT + 1):
        min_paths[i] = NODE_MAP[TG][i]  # 일단 첫 현재 상황을 TG 노드와 일치시켜준다

    cur_node = TG  # 일단 현재 노드는 여기인 건 맞으니 여기로 하겠음
    visited[cur_node] = 1
    sums = 1

    while sums < NODE_CNT:  # 모두 방문해서 판단했을 경우
        # visited 이 모두 다 끝날 경우
        cur_node = smallestIndex(cur_node, visited)
        visited[cur_node] = 1  # 결정된 애를 visited chck 해준다
        sums += 1

        # 이번 node 에서 할 일은, 지금까지 저장된 경로, 그리고 여기까지 온 상황에 대해서 생각해볼 것이다
        for k in range(1, NODE_CNT + 1):
            if NODE_MAP[cur_node][k] != 0 and visited[k] == 0:  # 방문할 수 있는 곳이여야 하며, 아직 방문하지 않은 곳이라면 판단한다
                # 지금까지 온 길 + 거기고 간 길 < 현재 가중치 일 경우 update 이 필요하다
                # 혹은 아직까지 도달하지 못했던 곳이면, min_paths == 0 이기 때문에, 최신화해주면 된다
                if min_paths[cur_node] + NODE_MAP[cur_node][k] < min_paths[k] or min_paths[k] == 0:
                    min_paths[k] = min_paths[cur_node] + NODE_MAP[cur_node][k]

    print(min_paths)


# 얘를 기준으로 계속 돌릴 것이다
'''현재 갈 수 있는 간선 중 제일 비용이 적은, 혹은 앞에 있는 node 로 가면 된다'''
'''그래야지 현재까지 저장된 경로가 그 경로까지 최소 경로임을 보장해준다 - 위에서 min_paths[cur_node] 가 현재까지 최소가 맞음이 보장'''
def smallestIndex(node, visited):
    tmp = NODE_MAP[node]  # 여기에서 제일 비용이 적은 node 로 갈 것인데, 방문한 것이면 안된다
    smallest = 100000000
    idx = 0
    for i in range(1, NODE_CNT + 1):
        if tmp[i] != 0 and visited[i] == 0:  # 연결이 되어 있고, 방문하지 않은 node 여야 한다
            smallest = min(tmp[i], smallest)
            idx = i
    return idx


# 2번 > PQ 를 사용해, NlogN 의 다익스트라를 구현해보아라


# 3번 > 이중배열을 사용하지 않고, 메모리가 최적화된 다익스트라를 구현해 보아라 ( 나는 일단 dict 로 하는 생각이 듬 )
pro1(1)
