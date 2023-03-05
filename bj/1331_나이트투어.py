import sys

sys.stdin = open("input_1331.txt")


def judge_available_positions(cur_pos):
    # 해당 포지션에서 갈 수 있는 위치들을 탐색
    # 갈 수 있는 위치들을 선정하고, 그 다음 것이 그 곳에 있는지를 확인하고 넘긴다.
    # 위치로 인한 제한, 이미 지나온 곳으로 인한 제한을 건다
    availables = []
    alphabet = ord(cur_pos[0]) - 64  # 알파벳
    number = int(cur_pos[1])  # 숫자
    da = [1, 2, 2, 1, -1, -2, -2, -1]
    dn = [2, 1, -1, -2, -2, -1, 1, 2]
    for i in range(len(da)):
        ma = alphabet + da[i]
        mn = number + dn[i]
        if 0 < ma < 7 and 0 < mn < 7:  # 가능하다면
            av = chr(ma + 64) + str(mn)
            if av not in trace:
                availables.append(av)
    return availables


T = int(input())

for _ in range(T):

    positions = []
    while True:
        try:
            pos = input()
            positions.append(pos)
        except:
            break

    trace = []  # 지난 곳들을 저장
    is_available = True

    # 아닐 경우 Invalid
    # 총 36 지점을 모두 지났을 경우 VALID

    for i in range(len(positions) - 1):
        if positions[i + 1] not in judge_available_positions(positions[i]):
            is_available = False
            break
        trace.append(positions[i])


    if is_available:  # 아직 가능하다면
        trace.clear()
        if positions[0] in judge_available_positions(positions[len(positions) - 1]):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
