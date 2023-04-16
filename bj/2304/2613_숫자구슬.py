# zzzzzzzzz ㅆㅃ!
import sys

sys.stdin = open("input_2613.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
marvels = list(map(int, input().split()))

# 요거 예외 TC 추가
if N == M:
    tmp = [1] * M
    print(max(marvels))
    print(*tmp)
    exit()


# 이렇게 된다면 경계 지점에서 무조건 M 개의 그룹을 이룬 상태일 것이다
# M 개가 될 수 없다면 (부족하다면) > 자연스러운 진행 후 True
# M 개가 될 수 있다면 > 무조건 M 개가 되도록 만들고 True
# M 개가 넘는다면 > 자연스러운 진행 False
def checker(limit):
    global each_node_cnts
    group_cnt = 0
    cur_sums = 0
    index = 0
    for i in range(len(marvels)):
        if marvels[i] > limit:
            return False
        tmp = cur_sums + marvels[i]
        if tmp > limit:
            group_cnt += 1
            cur_sums = marvels[i]

            each_node_cnts.append(index)
            index = 1
            # 넘길 때, 남은 그룹 갯수와 남은 index 수
            if M - group_cnt == len(marvels) - i:  # 현재 Node를 포함해서 더해주기 때문
                # 남은 갯수 만큼 1을 추가해주면 끝
                # 이미 이 조건을 탄다는거 자체가 된다는 거. break 가능
                for _ in range(M - group_cnt):  # 3번 만큼
                    each_node_cnts.append(1)  # 하나씩 들어가기 때문
                return True

        else:
            cur_sums += marvels[i]
            index += 1

    # 마지막 삐져 나온 녀석
    group_cnt += 1
    each_node_cnts.append(index)

    if group_cnt > M:  # limit 에 좀 더 여유를 줘야 함
        return False
    else:  # 그룹이 여유롭게 형성되거나, M 개가 나옴
        return True


def main():
    global each_node_cnts
    # 1이면,,,,
    # 이게 왜 꼭 max val 이여야 할까?
    lt = max(marvels) - 1
    # 최대 합은 모든 묶음
    rt = sum(marvels) + 1

    while lt + 1 < rt:  # 둘의 경계까지 가져오고, 경계 지점에서 끝낸다
        each_node_cnts = []
        mid = (lt + rt) // 2
        if checker(mid):  # limit 을 줄여서 아랫값쪽으로 더 확인을 한다
            rt = mid
        else:  # limit 을 늘려서 여유를 더 줘야 한다
            lt = mid

    each_node_cnts = []
    checker(rt)
    print(rt)
    print(*each_node_cnts)


main()
