import sys

sys.stdin = open("input_2805.txt")
input = sys.stdin.readline




# tg 으로 설정하고 tree 들을 잘랐을 때의 합이 M 이 되는가?
def is_height_ok(tg, M, trees):
    sum = 0
    for a in trees:
        if a - tg > 0:
            sum += (a - tg)
    if sum < M:
        return False
    return True


# 나무 수 N, 필요한 나무 길이 M
# > 제일 낮은것 부터, 제일 높은 곳까지가 노드
# > 높은걸 찾을때는, 가장 높은 범위 해주는게 낫다. O(N) 추가해주는 것보다
## 가능하다면 더 높게, 안된다면 더 낮게 설정하면서 나가면 된다
def solution(N, M, trees):
    # 범위는 언제나 mid 가 가능한 값 범위로
    hi = 2e9 + 1  # mid 가 2e9 일 수도 있음
    lo = -1  # mid 가 0 일 수도 있음
    while lo + 1 < hi:
        mid = (lo + hi) // 2  # 잘린 것의 합이 M 이 되는가?
        if is_height_ok(mid, M, trees):  # 가능하다면 좀 더 높게 설정해볼 수 있다
            lo = mid
        else:  # 안된다면 낮게 설정해본다
            hi = mid
    # 탈출 시점은 언제나 lo+1 = hi 일 때
    # 포함되어야 하면 답은 lo, 포함되면 안되면 hi
    # 이 경우는 lo, 왜냐하면 true 를 통과해야 하기 때문
    return lo


N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(int(solution(N, M, trees)))
