import sys

sys.stdin = open("input_3.txt")

T = int(input())


def DFS(node):
    if node == N + 1:
        print(used)
        return
    else:
        used.append(weights[node - 1])
        DFS(node + 1)
        used.remove(weights[node - 1])
        DFS(node + 1)


for _ in range(T):
    N = int(input())
    weights = list(map(int, input().split()))
    availables = []
    # 모든 부분집합을 고려한다.
    # 그 부분집합 내에서 합, 차를 모두 테스트 하여, availables 에 포함시킨다.
    used = []
    DFS(1)
