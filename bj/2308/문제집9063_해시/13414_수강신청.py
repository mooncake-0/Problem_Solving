import sys
from collections import deque


sys.stdin = open("input_13414.txt")
input = sys.stdin.readline
N, R = map(int, input().split()) # 몇 명인지, 몇 개 들어오는지
ranks = []
is_in = dict()

for rank_idx in range(R):
    stdnt = input().strip()
    if stdnt in is_in: # 들어 있으면 순위가 밀려난다. 현재 idx 기록대로 들어가게 한다
        is_in[stdnt] = rank_idx
    else: # d
        is_in[stdnt] = rank_idx
    ranks.append(stdnt)

cnt = 0
for idx in range(len(ranks)):
    if cnt == N:
        break
    if idx == is_in[ranks[idx]]: # 같으면 그 순위가 맞음
        print(ranks[idx])
        cnt+=1
