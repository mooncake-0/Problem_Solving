import sys


def build_tree(node, start, end):
    # 구간합을 기록, 만약 leaf node 확인시 기록
    if start == end:
        seg_tree[node] = tg[start]
    else:
        mid = (start + end) // 2
        build_tree(2 * node, start, mid)
        build_tree(2 * node + 1, mid + 1, end)
        seg_tree[node] = seg_tree[2 * node] + seg_tree[2 * node + 1]  # 만들고 현재 node 를 기록


# 범위 잘 생각해보기
# 그림 그리면 이해됨. 움직이는게 뭔지를 생각해야지..
def query(node, start, end, tg_st, tg_en):
    if tg_en < start or end < tg_st:
        return 0
    elif tg_st <= start and end <= tg_en:
        return seg_tree[node]
    else:  # 걸쳐졌을 경우, 탐색한다
        mid = (start + end) // 2
        left_sum = query(2 * node, start, mid, tg_st, tg_en)
        right_sum = query(2 * node + 1, mid + 1, end, tg_st, tg_en)
        return left_sum + right_sum


def update(node, start, end, idx, diff):
    # 범위를 벗어나면 탐색하지 않는다 (담당 idx 를 넘어갈 경우?)
    # 현재 탐색하고 있는 값이 st ~ end 인데, 이 영역을 idx 가 벗어날 경우
    if start > idx or end < idx:
        return

    # 포함구간이 있으면 해당구간을 바꾸고 후속 update 를 이어간다.
    seg_tree[node] += diff
    # 리프노드에선 중단해야지
    if start != end:
        mid = (start + end) // 2
        update(2 * node, start, mid, idx, diff)
        update(2 * node + 1, mid + 1, end, idx, diff)


input = sys.stdin.readline

N, M, K = map(int, input().split())
tg = []
for i in range(N):
    tg.append(int(input()))

# 이 시점에서 구간합 제어를 위한 seg_tree 생성 필요
seg_tree = [0] * (4 * len(tg))
build_tree(1, 0, len(tg) - 1)

for i in range(M + K):  # 명령이 들어오는 횟수
    a, b, c = map(int, input().split())
    if a == 1:  # 자리 바꾸기
        update(1, 0, len(tg) - 1, b - 1, c - tg[b - 1])
        tg[b - 1] = c
    elif a == 2:
        print(query(1, 0, len(tg) - 1, b - 1, c - 1))
