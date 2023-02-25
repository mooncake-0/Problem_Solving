import sys
from collections import deque

sys.stdin = open("input_7.txt")
T = int(input())

for _ in range(1, T + 1):

    order = input()
    order_q = deque(order)
    tc_num = int(input())
    tests = []
    for _ in range(tc_num):
        tests.append(input())

    for i in range(len(tests)):
        is_right = False
        for a in tests[i]:
            if len(order_q) == 0:
                is_right = True
                break
            if a == order_q[0]:
                order_q.popleft()
                if len(order_q) == 0:  # 마지막이 필수 수업인 경우
                    is_right = True
            elif a in order_q:  # 먼저 들었기 때문
                break
        if not is_right:
            print("#" + str(i + 1) + " NO")
        else:
            print("#" + str(i + 1) + " YES")
        order_q = deque(order)
