import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


print(board)