import sys

sys.stdin = open("input_5.txt")
N = int(input())
timeline = []
for i in range(N):
    s, e = map(int, input().split())
    timeline.append((s, e))

# tuple 다루기
timeline.sort(key=lambda x: (x[1], x[0]))
print(timeline)
cnt = 0
et = 0
for s, e in timeline:
    if s >= et:
        cnt += 1
        et = e
print(cnt)