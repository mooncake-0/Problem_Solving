'''
최대 질투심을 움직이면서,
사람이 몇명 모일 수 있는지를 판단해본다
N을 최대 질투심으로 판단했을때,
나올 수 있는 사람 수가 실제 사람 수보다 많다면, 최대 질투심을 늘려야 함
'''

import sys


## 이 방법대로 구하면 학생 수를 고정시킬 수가 없다
# 나누어 떨어지는 경우를 고려 안함
# 잘 좀 생각해라~!~!
def checker(tg, stones):
    cnt = 0
    for stone in stones:
        if stone > tg:
            cnt += (stone // tg)
            if stone % tg != 0:
                cnt +=1
        else:
            cnt += 1
    return cnt


def solution1(N, stones):
    # 질투심은 최대 1일 수 있다 (모두에게 한개만 나눠줌)
    # 질투심은 최대 max stone 갯수, 10e8 이다
    st = 0
    end = 10e8 + 1
    while st + 1 < end:
        mid = (st + end) // 2
        cnt = checker(mid, stones)
        if cnt > N:  # 질투심을 늘려야 한다
            st = mid
        else:  # 질투심을 줄일 수 있다 #
            end = mid

    return int(end)


sys.stdin = open("input_2792.txt")
input = sys.stdin.readline

# N<=10e8 M <= 300,000
N, M = map(int, input().split())
color_stone_cnt = []
for _ in range(M):
    color_stone_cnt.append(int(input()))
print(solution1(N, color_stone_cnt))
