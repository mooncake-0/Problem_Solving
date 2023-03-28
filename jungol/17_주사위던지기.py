'''
포인트
- 순열 조합 중복을 정리해보기 좋음
- 조합은 항상 헷갈린다 ㅠ.ㅜ
- 참고로 list.remove 는 발견되는 첫 수를 제거한다. 이 상황에선 pop 을 하는게 맞음
- 시간 복잡도를 생각하려면 list 막쓰기 보단 고정된 a= [0]*7 를 두고 쓰는게 좋음
- 왜냐하면 a[5] 이런식으로 indexing 하는게 three() 에서 사용된 in 절을 쓰는것보다
- 빠르기 때문이다

'''

import sys

sys.stdin = open("input_17.txt")
input = sys.stdin.readline


def one(n):
    global chosen
    if n < 1:
        print(*chosen)
        return
    else:
        for dice in range(1, 7):
            chosen.append(dice)
            one(n - 1)
            # 11123456
            # 121122
            chosen.pop()


# 순서와 상관없이 3가지를 고르는 경우의 수 6C3
def two(n, i):
    global chosen
    if n < 1:
        print(*chosen)
        return
    else:
        for dice in range(i, 7):
            chosen.append(dice)
            two(n - 1, dice)
            chosen.pop()


def three(n):
    global chosen
    if n < 1:
        print(*chosen)
        return
    else:
        for dice in range(1, 7):
            if dice not in chosen:
                chosen.append(dice)
                three(n - 1)
                chosen.pop()


def main():
    global chosen
    n, m = map(int, input().split())
    chosen = []
    if m == 1: one(n)
    if m == 2: two(n, 1)
    if m == 3: three(n)


main()
