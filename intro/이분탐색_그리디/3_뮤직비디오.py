import sys


def countSongs(std, nums):
    cnt = 0
    curSum = 0
    for i in range(0, len(nums)):
        tmp = curSum + nums[i]
        if tmp > std:
            cnt += 1
            curSum = nums[i]
        elif tmp == std:
            cnt += 1
            curSum = 0
        else:
            curSum = tmp
    if tmp != std:  # 딱 끝나는 것을 제외하면 항상 마지막 묶음이 있음
        cnt += 1
    return cnt


sys.stdin = open("input_3.txt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 어떤 특정한 값을 찾는다 --> 이분 검색을 해야겠다는 생각이 들면, lt, rt 선정이 우선

lt = 1  # 정답이 1분으로 나눠야 하는 것일 수도 있기 때문
rt = sum(nums)

while True:
    mid = (lt + rt) // 2
    eval = countSongs(mid, nums)
    if eval > m:
        lt = mid + 1
    elif eval == m:
        break
    else:
        rt = mid - 1

while True:
    tmp = mid - 1
    if m != countSongs(tmp, nums):
        print(mid)
        break
    else:
        mid = tmp
