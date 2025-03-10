N = int(input())
raw = []
for i in range(1, N + 1):
    raw.append(i)
print(raw)
seg_tree = [0] * (len(raw) * 4)


def build(s, e, idx):
    global seg_tree
    if s == e:  # mid 와 각자 기준이 같아짐
        seg_tree[idx] = raw[s]  # 이 값임
        return seg_tree[idx]
    mid = (s + e) // 2
    seg_tree[idx] = build(s, mid, 2 * idx) + build(mid + 1, e, 2 * idx + 1)  # 둘다 포함관계로 이동
    return seg_tree[idx]


build(0, len(raw) - 1, 1)


def get_sum(tg_s, tg_e, cover_s, cover_e, idx):
    # 지금 내가 커버하고 있는 구간을 벗어났으면 더해줄 필요 없음 (겹치는 구간이 없는 구간이면)
    # 각 미세한 노드들이 범위를 벗어나려고 함
    if cover_s > tg_e or cover_e < tg_s:
        return 0

    # 현재 Node 가 cover 하려는 영역이 tg 안에 들어오는 경우 (부분 완성 혹은 all 완성일 수도)
    # 이 Node 의 값을 사용한다
    if cover_s >= tg_s and cover_e <= tg_e:
        return seg_tree[idx]

    # 둘다 아니라면 분할해서 합을 가져와본다
    mid = (cover_s + cover_e) // 2
    return get_sum(tg_s, tg_e, cover_s, mid, 2 * idx) + get_sum(tg_s, tg_e, mid + 1, cover_e,
                                                                2 * idx + 1)  # 양 옆 노드로 보내면서 탐색한다
    # 사실 각 노드의 구간을 계속 똑같이 지정해주는거임!!! 1번 노드는 0~all, 2번노드는 앞쪽 반, 3번 노드는 뒷쪽 반


# 구간 합 구하기
# 2~4 까지의 구간합을 구한다고 하면, 역시 이분탐색으로 나아가면 됨.
# 전체 범위에 대해서, 내가 찾는 영역을 지정
# 현재 Node 필요 (init 고정) (트리의 이름)
# 현재 Cover 해보려는 구간 필요 (init 고정) (raw array) > 이게 계속 움직일거임
# 내가 원하는 구간 필요 (tg 지정)
print(get_sum(3, 7, 0, len(raw) - 1, 1))
