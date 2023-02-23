import sys

sys.stdin = open("input_7.txt")

N = int(input())
boxes = list(map(int, input().split()))
move_cnt = int(input())

for i in range(move_cnt):
    boxes.sort()
    boxes[N - 1] -= 1
    boxes[0] += 1

print(max(boxes) - min(boxes))
