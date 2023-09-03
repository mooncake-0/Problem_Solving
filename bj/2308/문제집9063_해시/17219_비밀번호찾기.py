import sys

sys.stdin = open("input_17219.txt")

N, M = map(int, input().split())

pws = dict()
for _ in range(N):
    hello = input().strip()
    tmp = hello.split()
    pws[tmp[0]] = tmp[1]
for _ in range(M):
    a = input().strip()
    print(pws[a])