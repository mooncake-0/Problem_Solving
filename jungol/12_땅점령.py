import sys
from collections import defaultdict

sys.stdin = open("input_12.txt")
input = sys.stdin.readline

N, play = map(int, input().split())

D = defaultdict(int)

for i in range(N):
    for j in range(N):
        D[(i, j)] = -1

print(D)