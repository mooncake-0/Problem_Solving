import sys

sys.stdin = open("input_2.txt")

N, find = map(int, input().split())
nums = []
for i in range(N):
    nums.append(int(input()))
print(nums)

lt = 1
rt = max(nums)

# mid 로 만들 수 있는 갯수 파악, 만들  수 있는 갯수가  11보다 적으면 아래로, 많으면 위로.
while True:
    mid = (rt + lt) // 2
    sum = 0
    for x in nums:
        sum += x // mid
    if sum == find:
        break
    elif sum > find:
        lt = mid + 1
    else:
        rt = mid - 1

while (True):
    check = mid + 1
    sum = 0
    for x in nums:
        sum += x // check
    if sum == find:
        mid = check
    else:
        print(mid)
        break
