import sys


# 1T -> 항상 이것보다 작아야 한다 했더니 계속 놓음..
def is_each_not_exceed_tg(tg, pos, stations):
    if len(stations) > 1:
        print(tg, pos, stations)
        for j in range(len(stations) - 1):  # 자신이 어떤 구간인지도 알긴 해야 함
            if stations[j] < pos < stations[j + 1]:  # 사이에서는 i 와 구해본다
                if stations[j + 1] - pos > tg or pos - stations[j] > tg:
                    return False
            else:  # 그 외는 아래와 같이 판단하면 station 사이의  거리가 나온다
                if (stations[j + 1] - pos) - (stations[j] - pos) > tg:
                    return False
    elif len(stations) == 1:
        if abs(stations[0] - pos) > tg:
            return False
    return True  # 없을 경우도 그냥 통과해라


# 2T -> 커지는 순간 놓는 것으로 변경해보자 (그럼 max 가 그 값임)
## 아니 이미 나뉜 구간중에 큰게 있으면 어쩌라고... 계속 추가한다 아님 그러면.. ㅠ 지금 구간 내 판단이 의미가 있나..?
## 구간이 제일 큰 곳 부터 찢어..?
## 현재 나뉜 구간 중 가장 큰 곳을 반으로 자르는걸 반복, tg 까지 자른 결과
## M 개 못놨으면 tg 줄여야함,(최댓값의 최솟값)
## M 개 이상 놨으면 tg 좀 더 키워야 한다 (M 개를 놔야 하기 때문)

## 풀다가 드는 생각인데.. 위치가 그닥 안중요한 것 같다. (가장 큰 녀석을 계속 잘라주면서 몇까지 가능한지만 알아내면..)
def find_max_with_index(cnt, lst):
    if not lst:
        return None, None  # 빈 리스트 처리
    max_idx = 0
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_idx = i
    return max_idx, max_val


def solution2(N, M, L, stations):
    stations.sort()
    st = 0  # 휴게소 위치는 중복되지 않는다
    end = L + 1  # 양 끝에 설치되어도 길이는 L
    while st + 1 < end:
        mid = (st + end) // 2  # 이 길이가 최소이다
        cnt = 0

        stations_dist = []
        for i in range(len(stations) - 1):  # i ~ i+1
            stations_dist.append(stations[i + 1] - stations[i])

        while True:
            idx, cur_max_val = find_max_with_index(cnt, stations_dist)
            print(cur_max_val, mid, stations_dist)
            if cur_max_val <= mid:  # 현재 최대값이 mid 보다 작아야 한다
                break
            # 돌아야 한다면, 둘을 반 자르고 다시 넣는다 (그 자리에 들어선것)
            stations_dist.pop(idx)
            val1 = cur_max_val // 2
            val2 = cur_max_val - val1
            stations_dist.append(val1)
            stations_dist.append(val2)
            cnt += 1

        if cnt < M:
            end = mid
        else:
            st = mid
    return st

# N,M,L -> 현재 갯수, 더 짓는 갯수, 도로 길이
# stations -> 현재 설치됨
def solution(N, M, L, stations):
    stations.sort()
    st = 0  # 휴게소 위치는 중복되지 않는다
    end = L + 1  # 양 끝에 설치되어도 길이는 L
    while st + 1 < end:
        mid = (st + end) // 2  # 이 길이가 최소이다.
        # 최댓값이 mid 야
        # 설치할 때 mid 를 넘지 않는 선에서 설치를 하고 왔을 때,
        # M 개를 다 설치 못했으면 최댓값을 줄여야 하고
        # M 개를 다 설치 했거나 남았으면 좀 늘려봐도 된다
        ## 중요한건 "매 지점에서 각 구간별 휴게소 거리를 판단해줘야 한다"
        cnt = 0
        added = []
        for i in range(1, L):  # 1 ~ L-1 설치
            # i 에 설치할 수 있는가?
            if is_each_not_exceed_tg(mid, i, stations) and is_each_not_exceed_tg(mid, i, added):
                added.append(i)
                cnt += 1
        if cnt >= M:
            st = mid
        else:
            end = mid
    return st, end


sys.stdin = open("input_1477.txt")
input = sys.stdin.readline

N, M, L = map(int, input().split())
stations = list(map(int, input().split()))
print(solution2(N, M, L, stations))
