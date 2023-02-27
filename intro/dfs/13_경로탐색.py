import sys

sys.stdin = open("input_13.txt")


def DFS(node):
    global cnt
    if node == pos:  # 5번에 도달을 했음!
        # print(visited)
        cnt += 1
        return
    else:
        for i in range(1, pos + 1):
            if matrix[node][i] == 1:  # 길이 있는 것
                if i not in visited:
                    visited.append(i)
                    DFS(i)
                    visited.remove(i)


T = int(input())

for _ in range(T):
    pos, path = map(int, input().split())
    matrix = [[0] * (pos + 1) for _ in range(pos + 1)]
    for _ in range(path):
        a, b = map(int, input().split())
        matrix[a][b] = 1
    cnt = 0
    visited = [1]
    DFS(1)
    print(cnt)
# DFS 노드의 의미가 뭔지 스스로 정확하게 세우고 가야한다
### 중요 -> DFS 내부 PARAM 의 정확한 의미, DFS 가 무슨 행위를 해주는지
# , 다음 DFS 는 어떤 노드로 이동을하는건지를 스스로 제대로 인지해야한다
