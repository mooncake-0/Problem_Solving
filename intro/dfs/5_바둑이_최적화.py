import sys

sys.stdin = open("input_5.txt")

''' # 4,5 에 대해 Timeout Error 발생
def DFS(node):
    global used
    if node >= len(weights):
        if sum(used) <= limit:
            sums.append(sum(used))
        return
    else:
        # 하는일
        used.append(weights[node])
        # 노드 분할
        DFS(node + 1)
        used.remove(weights[node])
        DFS(node + 1)


T = int(input())

for _ in range(T):
    limit, nums = map(int, input().split())
    weights = []
    for _ in range(nums):
        weights.append(int(input()))
    used = []
    sums = []
    DFS(0)
    print(max(sums))
'''


# 가지가 너무 많이 뻣어나갈 때는, 어떻게 하면 커팅해줄 수 있는지 판단해주는게 중요


# 강사 풀이
def DFS(node, sum, judged_weights_sum):
    global max_sum

    # 현재까지 더해진 수에 남은 모든 수가 다 포함된다 하더라도, 지금까지 나온 max_result 를 넘지 못한다고 판단되면
    if sum + (total - judged_weights_sum) < max_sum:  # ㅈ된다 ㅅㅂ..
        return

    if sum > limit:  # 더하고 나서 다음 노드로 들어가므로, 현재 일을 수행할 때 이미 sum 이 넘었으면, 해당 깊이 탐색을 종료한다
        return

    if node >= nums:
        # 결론이 나왔음
        if sum > max_sum:
            max_sum = sum
    else:
        DFS(node + 1, sum + weights[node], judged_weights_sum + weights[node])  # 지금까지의 sum에 현재 인덱스 값을 더한후, 다음 값으로 던져 줌
        DFS(node + 1, sum, judged_weights_sum + weights[node])  # 지금까지 판단한 수들의 합을 준다


T = int(input())

for _ in range(T):
    limit, nums = map(int, input().split())
    weights = []
    for _ in range(nums):
        weights.append(int(input()))
    max_sum = -99999999999
    total = sum(weights)

    ''' 처음부터 총 합이 더 작으면, 그냥 바로 총합을 출력한다 :: 완전히 틀리다 할 수는 없는데, DFS 에서 커팅할 수 있는 아이디어가 더 중요
    if sum(weights) <= limit:
        print(sum(weights))
    else:
    '''
    DFS(0, 0, 0)
    print(max_sum)
