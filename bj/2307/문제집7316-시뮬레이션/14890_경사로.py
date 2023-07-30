import sys

sys.stdin = open("input_14890.txt")
input = sys.stdin.readline

N, L = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

''' 짝 맞추기에 사용할 land 모양 '''
slope_land = []
tmp1 = []
tmp2 = [0]
for _ in range(L):
    tmp1.append(1)
    tmp2.append(1)
tmp1.append(0)
slope_land.append(tmp1)
slope_land.append(tmp2)
print(slope_land)
def is_same(array):
    eval = array[0]
    for i in range(len(array)):
        if array[i] != eval:
            return False
    return True

def sum_array(a1, a2):

    tmp = []
    for q in range(len(a1)):
        tmp.append(a1[q] + a2[q])
    print("summing",a1, a2, tmp)
    return tmp

def chunk_has_slope(chunk,  judger, i):
    for idx in range(len(chunk)):
        if judger[idx+i] != 0:
            return True
    return False

def judge_row_2(row):  # 모양을 먼저 만든다음에 매칭해보자
    judger = [0] * N
    slope = 0
    is_on_downside = False
    if N == L:
        if is_same(row):
            return True
        return False
    for i in range(N - L):
        chunk = row[i:i + L + 1]
        print(chunk)
        if L != 1:

            if is_same(chunk):  # 다 같은가?
                continue

            if chunk_has_slope(chunk, judger, i): # slope 구간이 있는가?
                # 단, 내려가는 구간에 대해서는 마지막 항에 대해서 체킹을 해야함
                if chunk[0] - chunk[1] == 1 and is_same(chunk[1:]):
                    pass
                if chunk[L] - chunk[L-1] == 1 and is_same(chunk[:L]):
                    return False
                else:
                    continue

            is_match = False

            for l in range(2):
                if is_same(sum_array(chunk, slope_land[l])):
                    if l == 0: # 오르막길
                        ra, rb = i, i+L
                    else: # 내리막길
                        ra, rb = i+1, i+L+1

                    for k in range(ra, rb):
                        # if judger[k]!= 1:
                        if l == 0:
                            judger[k] = 1
                        if l == 1:
                            judger[k] = -1
                        # else:
                        #     return False

                    is_match = True
                    if is_on_downside:
                        is_on_downside= False
                    break
            print("result judger", judger)
            if is_match:
                continue
            else:
                # is on downside 판단 필요
                if chunk[L-1] - chunk[L] == 1 and is_same(chunk[:L]):
                    is_on_downside = True
                    continue
                return False


        else:
            # arr 를 하나씩 읽으면서 기울기를 명시한다. 기울기가 바로 바뀌는 점 빼고 차이가 1이라면 다 가능
            if abs(row[i + 1] - row[i]) >= 2:
                return False
            # 내려갔다 올라오는건 안됨
            # 올라갔다 내려오는건 됨
            if row[i] > row[i + 1]:  # 내려감
                slope = -1
            elif row[i] < row[i + 1]:  # 올라감
                if slope == 0 or slope == 1:
                    slope = 1
                else:
                    return False
            else:
                slope = 0


    return True

def pro1():
    global cnt

    cnt = 0

    for x in field:
        result = judge_row_2(x)
        if result:
            cnt += 1
        print(x, result)

    for j in range(N):
        tmp = []
        for i in range(N):
            tmp.append(field[i][j])
        result = judge_row_2(tmp)
        if result:
            cnt += 1
        print(tmp, result)
    print(cnt)


def main():
    pro1()


main()