import sys, heapq

input = sys.stdin.readline

'''
아이디어가 제법 중요했던 문제
좀 걸렸음
'''

N = int(input())
l_arr = []  # max_heap
r_arr = []  # min_heap

# 기준을 먼저 마련하고 하나씩 넣어두자
if N == 1:
    print(int(input()))
elif N == 2:
    a = int(input())
    print(a)
    b = int(input())
    print(min(a, b))
else:
    a = int(input())
    print(a)
    b = int(input())
    stand = min(a, b)  # 현재 중앙값
    print(stand)
    if a >= b:
        l_arr.append(b * -1)
        r_arr.append(a)
    else:
        l_arr.append(a * -1)
        r_arr.append(b)

    for _ in range(N - 2):
        numb = int(input())
        if numb >= stand:
            heapq.heappush(r_arr, numb)
        else:
            heapq.heappush(l_arr, numb * -1)
        # 출력필요
        if len(l_arr) > len(r_arr):
            if abs(len(l_arr) - len(r_arr)) == 2:
                temp = heapq.heappop(l_arr) * -1
                heapq.heappush(r_arr, temp)
                stand = min(l_arr[0] * -1, r_arr[0])
                print(stand)
            else:  # == 1 일 경우만 온다
                stand = l_arr[0] * -1
                print(stand)
        elif len(l_arr) < len(r_arr):
            if abs(len(l_arr) - len(r_arr)) == 2:
                #  뽑아서 넣어주고 둘 중 비교해야함
                temp = heapq.heappop(r_arr)
                heapq.heappush(l_arr, temp * -1)
                stand = min(l_arr[0] * -1, r_arr[0])
                print(stand)
            else:  # == 1 일 경우만 온다
                stand = r_arr[0]
                print(stand)

        else:
            stand = min(l_arr[0] * -1, r_arr[0])
            print(stand)