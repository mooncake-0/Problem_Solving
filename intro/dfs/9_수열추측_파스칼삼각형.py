import sys

sys.stdin = open("input_9.txt")


# 미해결, 파스칼 삼각형 총 합 구하는 방법이 더 최적화 되어야 한다는데 개 이해가 안되어서 포기함
# 해당 배치에 대한 합을 구하는 N^2
def adding(the_list):
    while len(the_list) != 1:
        temp = []
        for i in range(len(the_list) - 1):
            temp.append(the_list[i] + the_list[i + 1])
        the_list = temp
    ''' 배치의 합을 구하는 방법을 좀 더 효율적으로 --> 규칙성 발견'''
    return the_list[0]


def DFS(node):
    global is_finished
    if is_finished:
        return
    if node > n:
        # 그 때 걸린 조합
        if adding(num_list) == final:
            is_finished = True
            print(num_list)
        return
    else:
        for x in range(1, n + 1):
            if x not in num_list:
                num_list.append(x)
                DFS(node + 1)
                num_list.remove(x)


T = int(input())

for _ in range(T):
    n, final = map(int, input().split())
    # n 개를 모두 일렬로 세우는 콤비네이션을 돈다
    num_list = []
    is_finished = False
    DFS(1)
