import sys

sys.stdin = open("input_10.txt")

T = int(input())


def DFS(node, start):
    if node > m:
        print(used)
        return
    else:
        for x in range(start, n + 1):
            print(x)
            used.append(x)
            DFS(node + 1, x + 1)
            used.remove(x)

# 조합은 3, 1 을 뽑든 1, 3 을 뽑든 같은 건으로 간주
#

for _ in range(T):
    n, m = map(int, input().split())
    used = []
    DFS(1, 1)
