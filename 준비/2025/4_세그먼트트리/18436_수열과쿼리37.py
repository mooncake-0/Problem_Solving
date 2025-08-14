import sys

input = sys.stdin.readline


def build_even(node, start, end):
    if start == end:
        if arr[start] % 2 == 0:
            even_tree[node] = 1
    else:
        mid = (start + end) // 2
        build_even(2 * node, start, mid)
        build_even(2 * node + 1, mid + 1, end)
        even_tree[node] = even_tree[2 * node] + even_tree[2 * node + 1]


def build_odd(node, start, end):
    if start == end:
        if arr[start] % 2 != 0:
            odd_tree[node] = 1
    else:
        mid = (start + end) // 2
        build_odd(2 * node, start, mid)
        build_odd(2 * node + 1, mid + 1, end)
        odd_tree[node] = odd_tree[2 * node] + odd_tree[2 * node + 1]


# 범위 또 틀림.. 움직이는게 뭔지 항상 생각
def query(tg_tree, node, start, end, s_idx, e_idx):  # 구간내 n 개
    # st~end 가 범위 밖일 경우
    if end < s_idx or start > e_idx:
        return 0
    elif s_idx <= start and end <= e_idx:
        return tg_tree[node]
    else:
        mid = (start + end) // 2
        left_sum = query(tg_tree, 2 * node, start, mid, s_idx, e_idx)
        right_sum = query(tg_tree, 2 * node + 1, mid + 1, end, s_idx, e_idx)
        return left_sum + right_sum


def update_even(node, start, end, idx, is_removing):  # 바뀐값이 홀수냐 짝수냐에 따라 계산 변경
    # 바뀐 녀석 담당하는 구간이 아니라면
    if idx < start or idx > end:
        return
    # 포함되어 있는 구간이니 변경을 수행한다
    if is_removing:
        even_tree[node] -= 1
    else:
        even_tree[node] += 1

    # 다음 구간으로 넘긴다
    if start != end:
        mid = (start + end) // 2
        update_even(2 * node, start, mid, idx, is_removing)
        update_even(2 * node + 1, mid + 1, end, idx, is_removing)



def update_odd(node, start, end, idx, is_removing):  # 바뀐값이 홀수냐 짝수냐에 따라 계산 변경
    # 바뀐 녀석 담당하는 구간이 아니라면
    if idx < start or idx > end:
        return
    # 포함되어 있는 구간이니 변경을 수행한다
    if is_removing:
        odd_tree[node] -= 1
    else:
        odd_tree[node] += 1

    # 다음 구간으로 넘긴다
    if start != end:
        mid = (start + end) // 2
        update_odd(2 * node, start, mid, idx, is_removing)
        update_odd(2 * node + 1, mid + 1, end, idx, is_removing)


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
even_tree = [0] * (4 * len(arr))
odd_tree = [0] * (4 * len(arr))

build_even(1, 0, len(arr) - 1)
build_odd(1, 0, len(arr) - 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:  # b 번째 수를 c  로 바꿈 (제일 어렵다) (걔가 포함된 친구들은 다 바뀌어야함)
        # 짝수 였던 녀석 -> 홀수로
        if arr[b - 1] % 2 == 0 and c % 2 != 0:
            update_even(1, 0, len(arr) - 1, b - 1, True)
            update_odd(1, 0, len(arr) - 1, b - 1, False)
        # 홀수 였던 녀석 -> 짝수로
        if arr[b - 1] % 2 != 0 and c % 2 == 0:
            update_even(1, 0, len(arr) - 1, b - 1, False)
            update_odd(1, 0, len(arr) - 1, b - 1, True)
        # 실제 바꿔야 함 (나머지는 안바꿔도 된다)
        arr[b - 1] = c
    elif a == 2:  # b번째 수 ~ c번째 수 사이에 짝수 갯수
        print(query(even_tree, 1, 0, len(arr) - 1, b - 1, c - 1))
    else:  # 홀수 갯수
        print(query(odd_tree, 1, 0, len(arr) - 1, b - 1, c - 1))
