import sys

sys.stdin = open("input_12.txt")

T = int(input())

# 인접 행렬 (aij 면 i --> j 로 이동 가능함을 말한다)
# 경로탐색을 위한 사전학습
for _ in range(T):
    ''' # 기본 인접 행렬 2, 4 라 되어 있으면 2->4, 4->2 매트릭스를 1 로 표현
    pos, lines = map(int, input().split())
    avail = []
    for _ in range(lines):
        avail.append(list(map(int, input().split())))
    matrix = [[0] * 6 for _ in range(6)]

    for a, b in avail:
        matrix[a][b] = 1
        matrix[b][a] = 1

    for x in matrix:
        print(x)
    '''
    pos, lines = map(int, input().split())
    matrix = [[0] * (pos + 1) for _ in range(pos + 1)]
    for _ in range(lines):
        a, b, c = map(int, input().split())
        matrix[a][b] = c

    for i in range(1, pos + 1):
        for j in range(1, pos + 1):
            print(matrix[i][j], end=" ")
        print()
