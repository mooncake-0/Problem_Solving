import sys
from heapq import *

sys.stdin = open("input_35.txt")
input = sys.stdin.readline

'''
포인트
    - 힙을 사용하는 센스
    - 중앙 기점으로 양 옆으로 돌리는 자료구조 -> 메모장 문제와 유사

'''

# 중앙값에 대한 주시 > 일단 고도화시 PQ 에 대한 의심을 해볼 필요 있음
# 그냥 풀면 쉬움. 하지만 딱봐도 TO 나게 생김

def pro2():  # 아래는 O(4억) 정도, fail 나야 정상
    # 중앙값을 계속 바라보자.
    # 양옆으로 나누는 느낌 살짝 오는 듯.
    # 좌측에는 작은값이 들어오는데, 제일 큰 값을 뱉어내야 한다. max hq
    # 우측에는 큰 값들이 들어오므로, 제일 작은 값을 뱉어내야 한다. min hq
    center = int(input())
    print(center)
    left_max_hq = []
    right_min_hq = []

    # 약 (M) * N*logN 정도의 시간 복잡도 (훨씬 빠름)
    for i in range(N // 2):
        # 이렇게 돌릴 때, s, e 를 판단한다
        # center 보다 작으면 lmh 에, center 보다 크면 rmh 에 넣겠다.
        # 두 사이즈가 같으면 잘 들어간것
        # 두 사이즈가 다르면 한쪽에 쏠린 것. 둘 중에 size 2 인 것에서 하나를 뽑는다.
        # 뽑힌게 Center 가 되고, Center 였던 애는 반대촉으로 heappush
        s, e = map(int, input().split())
        if s < center: heappush(left_max_hq, -s)
        if s > center: heappush(right_min_hq, s)
        if e < center: heappush(left_max_hq, -e)
        if e > center: heappush(right_min_hq, e)
        # 4O(log(n) 정도)

        if len(left_max_hq) > len(right_min_hq):  # 둘다 center 보다 작은 값이였음
            tmp = -1 * heappop(left_max_hq)
            heappush(right_min_hq, center) #log(n)
            center = tmp
        elif len(left_max_hq) < len(right_min_hq):  # 둘다 center 보다 큰 값이였음
            tmp = heappop(right_min_hq)
            heappush(left_max_hq, -center) # log(n)
            center = tmp
        print(center)


def pro1():
    global picked
    first = int(input())
    picked.append(first)
    print(first)
    # O(1/2 * N)
    for i in range(N // 2):
        s, e = map(int, input().split())
        picked.append(s)
        picked.append(e)
        picked.sort()  # O(NlogN)
        print(picked[len(picked) // 2])
    # MAX 400,000,000 # 4억인데? 어케 통과했누;


def main():
    global N, picked
    N = int(input())
    picked = []
    pro2()


main()
