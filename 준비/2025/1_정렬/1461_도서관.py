import sys

'''
아이디어 싸움. 이런 왔다 갔다 혹은 크고 작은 느낌 -> 정렬에 대한 생각
'''


input = sys.stdin.readline


def pop_M(M, tg):
    global anw
    while len(tg) >= M:
        anw += tg[-1] * 2
        for i in range(M):
            tg.pop()
    if tg:
        anw += tg[-1] * 2


def find_least_movement(M, positions):

    global anw
    anw = 0
    arr_pos = sorted([x for x in positions if x >= 0])
    arr_neg = sorted([-1 * x for x in positions if x < 0])

    # 누가 더 큰지만 일단 정해둔다
    max_pos = 0
    max_neg = 0
    if arr_pos:
        max_pos = arr_pos[-1]
    if arr_neg:
        max_neg = arr_neg[-1]

    # arr 가 다 빠질 때까지 M 개씩 계속 빼준다
    pop_M(M, arr_pos)
    pop_M(M, arr_neg)

    # 마지막에 더 큰쪽이였던 곳에서 max 값이였던 것을 빼준다
    if max_pos >= max_neg:
        anw -= max_pos
    else:
        anw -= max_neg
    return anw


N, M = map(int, input().split())
positions = list(map(int, input().split()))
print(find_least_movement(M, positions))
