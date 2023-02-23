import sys

sys.stdin = open("input_8.txt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
last_index = -1
cnt = 0
not_finished = False

while True:
    if len(nums) <= 1:
        if len(nums) == 1:
            cnt += 1
        break
    if nums[0] + nums[last_index] <= m:
        nums.remove(nums[0])
        nums.remove(nums[last_index])
        last_index = -1
        cnt += 1
    else:
        last_index -= 1
        if last_index * -1 == len(nums):
            not_finished = True
            break

if not_finished:
    cnt += len(nums)
print(cnt)
