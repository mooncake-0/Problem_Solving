import sys

input = sys.stdin.readline
N = int(input())


# X 에서 할 수 있는 연산 3가지
# X 가 3으로 나누어 떨어지면 3으로 나눈다
# X 가 2로 나누어 떨어지면 2로 나눈다
# 1을 뺀다

# BFS 하면 무조건 시간 초과될 것이 보임, 시간 제한이 너무 타이트하기 때문 (0.7초)
# DP 로 접근해보자
# 1 > 0
# 2 > 1
# 3 > 1 // 3으로 나눈다
# 4 > 2 // 1을 빼고 3으로 나눈다 // 2를 두번 나눈다 // 2로 나누고 1을 뺀다
# 5 > 3 (4방법 +1)
# 6 > 2
# 7 > 3 (6방법 +1)
# 8 > 3 (4방법 +1)
# 9 > 2 (3방법 + 1)
# 10 > 3 (9방법 + 1)


# 수의 연속
# 3
# 3의 배수 다음수 4 (3의 배수방법 +1)
# 1번의 다음수 5 (1번의 방법 +1)
# 3의 배수 6 (3으로 나눈 녀석의 방법 + 1)

# BUP
def pro1():
    fn = [0] * (N + 1)
    if N == 1:
        print(0)
        return
    if N == 2:
        print(1)
        return
    if N == 3:
        print(1)
        return

    fn[1] = 0
    fn[2] = 1
    fn[3] = 1

    for i in range(4, len(fn)):
        # 수는 3가지 경우가 있다
        # 3의 배수 다음 수
        if i % 3 == 1:
            if i % 2 == 0:
                fn[i] = min(fn[i - 1], fn[i // 2]) + 1
            else:
                fn[i] = fn[i - 1] + 1
        # 그 다음 수
        elif i % 3 == 2:  # 그 전거에서 1 빼는 방법
            # 그 중 2로 나누어 떨어지는 애가 있음
            if i % 2 != 0:
                fn[i] = fn[i - 1] + 1
            else:  # 8 같은 놈. 이 친구는 //2 하는게 더 빠른 방법
                fn[i] = fn[i // 2] + 1

        else:
            if i % 2 == 0:
                fn[i] = min(fn[i // 3], fn[i // 2]) + 1
            else:
                fn[i] = fn[i // 3] + 1

    print(fn[N])


def main():
    pro1()
    # pro2()


main()
