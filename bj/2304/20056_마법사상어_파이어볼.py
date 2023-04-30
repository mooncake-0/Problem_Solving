import sys

sys.stdin = open("input_20056.txt")
input = sys.stdin.readline

'''

포인트
    - 뭐 없음... 그냥... ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 열심히 구현한거라 ... 
    - 짝수 홀수 판단 기준..... 때문에 계속 안되었음.... 아쉽.. 

'''

def moveFb(fi, fj, fm, fs, fd):  # 해당 dir 으로 ㄱㄱ
    mi = fi + dir_map[fd][0] * fs
    mj = fj + dir_map[fd][1] * fs
    # 4*4 가 있는데, 이 때, %4 를 한다면?
    if mi < 1:
        mi = abs(mi)
        mi = N - (mi % N)
    elif mi > N:
        mi %= N
        if mi == 0:
            mi += N

    if mj < 1:
        mj = abs(mj)
        mj = N - (mj % N)
    elif mj > N:
        mj %= N
        if mj == 0:
            mj += N
    return (mi, mj)


def main():
    global K, fInfo, fValid
    while K != 0:

        move_pos = dict()

        # 각 FB 가 움직일 곳이 정해진다
        for fIdx in range(1, len(fInfo)):  # fInfo 에 저장되어 있는 f 정보들을 토대로 움직이게 한다
            if fValid[fIdx] != 1:
                continue
            pos = moveFb(*fInfo[fIdx])
            # 해당 포지션으로 이동하는 FB 들을 확인한다
            if pos in move_pos:
                move_pos[pos].append(fIdx)
            else:
                move_pos[pos] = [fIdx]

        # 움직임 MAP 대로 이동을 수행한다
        for m in move_pos:

            if len(move_pos[m]) != 1:  # 겹친다 # 겹치면 분화해야지
                # 그 인덱스의 애들을 모두 모으고 모아요 > fINFO 에 더해주면 된다.
                sum_m = 0
                sum_v = 0

                is_odd = 0
                is_even = 0

                for fIdx in move_pos[m]:
                    sum_m += fInfo[fIdx][2]
                    sum_v += fInfo[fIdx][3]

                    if fInfo[fIdx][4] % 2 == 0:
                        is_even += 1
                    else:
                        is_odd += 1

                    fValid[fIdx] = 0  # 합쳐지는 애들을 모두 제거한다

                # 질량이 5 이하면 생성되지 않는다
                if sum_m >= 5:
                    if is_even == len(move_pos[m]) or is_odd == len(move_pos[m]):
                    # if sum_d % 2 == 0:
                        ed = [0, 2, 4, 6]
                    else:  #
                        ed = [1, 3, 5, 7]
                    for d in ed:  # 4개를 추가한다
                        fInfo.append([m[0], m[1], sum_m // 5, sum_v // len(move_pos[m]), d])
                        fValid.append(1)

            else:  # 겹치지 않으니 그냥 움직여 준다
                fInfo[move_pos[m][0]][0] = m[0]  # 얘의 정보
                fInfo[move_pos[m][0]][1] = m[1]
        K -= 1

    sum_m = 0
    for x in range(0, len(fInfo)):
        if fValid[x] == 1:
            sum_m += fInfo[x][2]
    print(sum_m)


N, M, K = map(int, input().split())
dir_map = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}

fValid = [0] * (M + 1)
fInfo = [0]
for fidx in range(1, M + 1):
    tmp = list(map(int, input().split()))
    fInfo.append(tmp)
    fValid[fidx] = 1

main()
