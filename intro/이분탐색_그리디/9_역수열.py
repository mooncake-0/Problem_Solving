import sys

sys.stdin = open("input_9.txt")

n = int(input())
nums = list(map(int, input().split()))
original = [0] * n

for i in range(len(nums)):
    zeroes = 0
    for j in range(len(original)):
        if zeroes == nums[i]:
            if original[j] == 0:
                original[j] = i + 1
                break
        if original[j] == 0:
            zeroes += 1

print(original)
