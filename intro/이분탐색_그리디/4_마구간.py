import sys

sys.stdin = open("input_4.txt")


def findHorse(distance):
    cnt = 1  # 말 갯수
    closest_horse = houses[0]
    for i in range(1, n):
        if houses[i] - closest_horse >= distance:  # 배치 가능하면 배치한다
            closest_horse = houses[i]
            cnt += 1
    return cnt


n, c = map(int, input().split())
houses = []
for i in range(n):
    houses.append(int(input()))
houses.sort()

lt = 1  # 말 사이의 최소 거리는 1일 것이다
rt = houses[n - 1] - 1  # 맨 마지막에 있는 마굿간이 최대 거리 (단순히 두 말 사이가 가질 수 있는 최대 거리)

while True:
    mid = (lt + rt) // 2  # 두 거리의 중간값
    cnt_horse = findHorse(mid)
    if cnt_horse > c:  # 이 거리로 두었을 때 배치할 수 있는 말의 최대 수가 넘으면 말이 너무 많음
        lt = mid + 1
    elif cnt_horse == c:
        res = mid  # 일단 얘가 되면 답의 범위에 들어옴
        break
    else:  # 말이 부족하면 거리를 좀 줄여야 한다
        rt = mid - 1

while True:
    cnt_horse = findHorse(res + 1)
    if cnt_horse != c:  # 하나씩 올리면서 최대 거리를 찾는다.
        print(res)
        break
    else:
        res += 1
