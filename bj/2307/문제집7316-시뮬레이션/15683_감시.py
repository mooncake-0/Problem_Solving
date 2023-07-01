import sys


sys.stdin = open("input_15683.txt")
input = sys.stdin.readline

# 1  > 한 방향, 2> 양방향, 3> 90도 방향, 4> 세방향, 5> all
I, J = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(I)]



for x in room:
    print(x)


def pro1():
    pass


def main():
    pro1()


main()