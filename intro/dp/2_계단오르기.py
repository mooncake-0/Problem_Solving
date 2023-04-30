import sys

# 한번에 한계단 or 두 계단. N 계단 오르는 경우의 수  (N <45)
N = int(input())


#
# a 계단까지 올라왔음
# a-1 계단 까지올라온 방법에 + 1 계단
# a-2 계단까지 올라온 방법에 + 2 계단이므로 (두가지 방법씩이 추가된다)
# 하지만 중복이 있음 # a-2 계단까지 올라온 방법에서 +1 을 하는 방법은 a-1 과의 중복
# 따라서 a-2 계단까지에서 +2 와, a-1 계단까지에서 +1 계단씩이 있는 것.
# 즉, 피보나치

# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# f(5) = 8
# f(6) = 13
# f(7) = 21

# BUP
def pro1():
    pro = [0] * (N + 1)
    pro[1] = 1
    pro[2] = 2
    for i in range(3, len(pro)):
        pro[i] = pro[i - 1] + pro[i - 2]
    print(pro[N])


def rec(tg):
    # MEMOIZATION 사용
    global pro
    if pro[tg] != 0:
        return pro[tg]
    if tg == 1 or tg == 2:
        return tg
    pro[tg] = rec(tg-1) + rec(tg-2)
    return pro[tg]

# TDP > MEMOIZATION 중요 > 재귀
def pro2():
    global pro
    pro = [0] * (N + 1) # MEMOIZATION 안 쓰면 40 정도부터 TOE
    print(rec(N))


def main():
    pro1()
    pro2()


main()