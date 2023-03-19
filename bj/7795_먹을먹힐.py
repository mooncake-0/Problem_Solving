import sys

for _ in range(int(input())):
    len_A, len_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    # NAIVE 하게
    # # N, M ~ 20000 까지 가능
    # # N^2 을 기본적으로 돈다
    # for i in range(len_A):
    #     for j in range(len_B):
    #         if A[i] > B[j]:
    #             cnt += 1
    # print(cnt)

    # 시간 복잡도 생각해보면 # NlogN
    B.sort(reverse=True)
    # 소팅된 상태라고 가정해보자.
    # 11
    # 136
    # N^(N-x)
    for i in range(len_A):
        for j in range(len_B):
            if A[i] > B[j]:
                cnt += (len_B -j)
                break
    print(cnt)

    # 둘 다 소팅된 상태라면?
    # 1137810
    # 23678