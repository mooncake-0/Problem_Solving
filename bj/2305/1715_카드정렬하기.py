import sys
from heapq import *

sys.stdin = open("input_1715.txt")
input = sys.stdin.readline

'''
포인트
    - 내가보기엔 그리디는 "특정한 가정을 세우고 문제를 푸는 것"
    - 돌려보다가 반례 생각 > 가정이 틀릴 수도 있다는 것을 알 수도 있
    - 수정 / 신규 가정
'''

'''
작은 것부터 진행한다가 맞는것.. 같은데
'''


# 반례 # 10, 100, 101, 102 일 경우, 더 작은 경우가 있음
def pro1():
    N = int(input())
    if N == 1:
        print(0)
        return
    nums = []
    for i in range(N):  # O(N)
        nums.append(int(input()))
    nums.sort()  # O(N)

    sums = [0] * (N)  # 000
    sums[0] = nums[0] + nums[1]  # 30 00

    for i in range(1, N - 1):  # 1,2 에 대해
        sums[i] = sums[i - 1] + nums[i + 1]
    print(sum(sums))


'''
생각은 맞게 접근했는데, 그게 돌아가는 과정을 조금 더 생각했으면 좋겠음
>> "왜 안되는가?" 를 생각해내는게 항상 어려운 듯
'''


# 카드덱을 계속 섞는다. 그리고 현재 남아 있는 카드덱 중 가장 작은 두개를
# 합치면서 나아가야 한다
def pro2():
    # HEAP 을 사용해서 가장 작은 녀석들 두개가 튀어나오게 한다
    # used 를 사용해서 사용된 녀석인지 판별을 한다
    N = int(input())
    if N == 1:
        print(0)
        return
    nums = []
    for i in range(N):  # O(N)
        nums.append(int(input()))

    hq = []
    for i in range(N):
        heappush(hq, (nums[i], i))

    anw = 0
    repeat = 0
    while repeat < N - 1:  # 5개를 돌리면 4번. N 개를 돌리면 N-1 번
        a, idxa = heappop(hq)
        b, idxb = heappop(hq)
        nums[idxa] = a + b
        nums[idxb] = -1  # 사용하지 않는 값으로 넣는다
        heappush(hq, (nums[idxa], idxa))
        anw += a + b
        repeat += 1
    print(anw)


def main():
    # pro1()
    pro2()


main()
