import sys

'''
포인트
- 연습정도의 문제. 주사위 던지기 1 이 더 중요함
'''

sys.stdin = open("input_19.txt")
input = sys.stdin.readline


def throw(cnt):
    global k, using, total
    if cnt > k:
        if sum(using) == total:
            print(*using)
        return
    else:
        for i in range(1, 7):
            using[cnt - 1] = i
            throw(cnt + 1)
            using[cnt - 1] = 0


def main():
    global k, using, total
    k, total = map(int, input().split())
    using = [0] * k
    throw(1)


main()
