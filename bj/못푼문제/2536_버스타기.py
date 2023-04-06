# 어차피 이중배열로 못푼다
# m, n = 100,000
# m*n = 10,000,000,000 # 100얶!
# 마킹하고 이중 배열 탐색하고 그러는걸로는 절대 못품

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def pro2(depx, depy, destx, desty):
    used_bus = [0] * (bus_num + 1)

    dq = deque()
    dq.append(((depx, depy), 0))

    while dq:
        cur_position, cur_bus_cnt = dq.popleft()

        if cur_position == (destx, desty):
            print(cur_bus_cnt)
            return

        # CUR_POSITION 의 v, h 라인에서 각각 운행하는 버스 리스트들
        # TODO CUR_POSITION 을 지나는지 확인 필요함
        h_buses = busline_dict[(cur_position[0], 0)]  # 현재 포지션과 horizontal 하게 운행하는 버스들
        v_buses = busline_dict[(0, cur_position[1])]

        for bus_index in h_buses:
            if used_bus[bus_index] == 1:  # 사용되었다면
                continue
            a = buses[bus_index][0]  # 버스의 시작점 (2,1)
            b = buses[bus_index][1]  # 버스의 종착점 (2,6)
            if a[1] > b[1]: a, b = b, a  # b 가 더 높게 세팅

            if a[1] <= cur_position[1] <= b[1]:  # 이 경우에만 해당 버스를 사용하는 것
                for v in range(a[1], b[1] + 1):  # 갈 수 있는 각 지점들을 추가해줄 것이다
                    # a[1] 은 현재 지점이므로, +1 을 해준다
                    if v != cur_position[1]:
                        dq.append(((cur_position[0], v), cur_bus_cnt + 1))
                # 사용된 버스를 체크한다
                used_bus[bus_index] = 1

        for bus_index in v_buses:
            if used_bus[bus_index] == 1:  # 사용되었다면
                continue
            a = buses[bus_index][0]  # (1,5)
            b = buses[bus_index][1]  # (7,5)
            if a[0] > b[0]: a, b = b, a  # b 가 더 높게 세팅

            if a[0] <= cur_position[0] <= b[0]:
                for h in range(a[0], b[0] + 1):
                    if h != cur_position[0]:
                        dq.append(((h, cur_position[1]), cur_bus_cnt + 1))
                # 사용된 버스를 체크한다
                used_bus[bus_index] = 1


### 틀린 점 1) 내가 서 있는 지점이 아닌 곳에 버스가 지날 수도 있는데, 그 지점들도 추가된다.
### 탔던 버스의 종류 등이 고려 되지 않았다.
### 시간 초과 또한 발생. 사실 usage 된 애들 제거하는 방식의 O를 낮출 수만 있어도 TO 은 피할 수 있을 듯
def pro1(depx, depy, destx, desty):
    dq = deque()
    dq.append(((depx, depy), 0))  # 현재 위치 , 탑승한 버스 수

    in_use = []
    in_use.append((depx, depy))

    while dq:
        cur_position, cur_bus_cnt = dq.popleft()

        # print(cur_position, cur_bus_cnt)

        if cur_position == (destx, desty):
            print(cur_bus_cnt)
            return

        # 탈 수 있는 버스들에 대한 탐색
        # 1 번 가로축에 대해, 2번 세로축에 대해
        h_buses = busline_dict[(cur_position[0], 0)]
        v_buses = busline_dict[(0, cur_position[1])]

        # print(h_buses)
        # print(v_buses)
        # 각 버스들을 탔을 경우
        # vertical 하게 움직이는 위치들을 파악해야 한다
        for bus_index in h_buses:
            a = buses[bus_index][0]
            b = buses[bus_index][1]
            if a[1] > b[1]: a, b = b, a  # b 가 더 높게 세팅

            for v in range(a[1] + 1, b[1] + 1):
                if (cur_position[0], v) not in in_use:
                    # if ((cur_position[0], v), cur_bus_cnt + 1) not in dq:
                    in_use.append((cur_position[0], v))
                    dq.append(((cur_position[0], v), cur_bus_cnt + 1))  # 모든 지점들을 탐색한다

        for bus_index in v_buses:
            a = buses[bus_index][0]
            b = buses[bus_index][1]
            if a[0] > b[0]: a, b = b, a  # b 가 더 높게 세팅

            for h in range(a[0] + 1, b[0] + 1):
                if (h, cur_position[1]) not in in_use:
                    # if ((h, cur_position[1]), cur_bus_cnt + 1) not in dq:
                    in_use.append((h, cur_position[1]))
                    dq.append(((h, cur_position[1]), cur_bus_cnt + 1))  # 모든 지점들을 탐색한다

    # 탈 수 있는 버스들에 대한 탐색 >
    print(-1)


# buses ~ 5000
def main():
    global buses, busline_dict, bus_num
    X, Y = map(int, input().split())
    bus_num = int(input())
    buses = [0]
    busline_dict = defaultdict(list)
    # busline_dict = dict()

    for i in range(1, bus_num + 1):
        num, sx, sy, ex, ey = map(int, input().split())
        buses.append(((sx, sy), (ex, ey)))
        key = ()
        if ex - sx == 0:  # x = ex 에서 세로로 다니는 애
            key = (ex, 0)
        else:  # y = ey 에서 가로로 다니는 애
            key = (0, ey)

        # 처음이면 그냥 추가한다
        if key not in busline_dict:
            busline_dict[key] = [i]
        # 처음이 아니면 뒤에 추가하는데,
        # 포함구간안에 있는 버스라면 포함시키지 않는다
        else:

            add = True

            for bus_idx in busline_dict[key]:
                pre = buses[bus_idx]  # 기존 친구
                new = buses[i]  # 새 친구

                if key[0] != 0:  # 세로로 다니는 애

                    if new[0][1] >= pre[0][1] and new[1][1] <= pre[1][1]:  # 비추가 대상
                        add = False
                    elif pre[0][1] >= new[0][1] and pre[1][1] <= new[1][1]:  # 교체 대상
                        add = False
                        busline_dict[key].remove(bus_idx)
                        busline_dict[key].append(i)
                        break
                else:  # 가로로 다니는 애

                    if new[0][0] >= pre[0][0] and new[1][0] <= pre[1][0]:  # 비추가 대상
                        add = False
                    elif pre[0][0] >= new[0][0] and pre[1][0] <= new[1][0]:  # 교체 대상
                        add = False
                        busline_dict[key].remove(bus_idx)
                        busline_dict[key].append(i)
                        break
            if add:
                busline_dict[key].append(i)

    depx, depy, destx, desy = map(int, input().split())

    # print(buses)
    # print(busline_dict)
    # print("=================================================")

    # pro1(depx, depy, destx, desy)
    pro2(depx, depy, destx, desy)


main()
