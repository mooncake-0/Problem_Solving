import sys

sys.stdin = open("input_11.txt")

T = int(input())


def DFS(node, start):
    if node > m:
        sum_list.append(sum(used))
        return
    else:
        for i in range(start, n):
            used.append(nums[i])
            DFS(node + 1, i + 1)
            used.remove(nums[i])


for _ in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    multiple = int(input())
    sum_list = []
    used = []
    DFS(1, 0)
    cnt = 0
    for x in sum_list:
        if x % multiple == 0:
            cnt += 1
    print(cnt)
