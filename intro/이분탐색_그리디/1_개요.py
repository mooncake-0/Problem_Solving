import sys

sys.stdin = open("input_1.txt")

n, find = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lt = 0
rt = len(nums) - 1

while (True):
    mid = (lt + rt) // 2
    if nums[mid] == find:
        print(mid+1)
        break
    elif nums[mid] > find:
        rt = mid - 1
    else:
        lt = mid + 1
