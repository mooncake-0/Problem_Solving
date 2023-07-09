import sys

sys.stdin = open("input_18808.txt")
input = sys.stdin.readline

# I, J - 1 ~ 40
# K - 100
I, J, K = map(int, input().split())
labtop = [[0] * J for _ in range(I)]

# 모눈종이 사이즈 1~10
stickers = []
size = []
for _ in range(K):
    a, b = map(int, input().split())
    size.append((a, b))
    sticker = [list(map(int, input().split())) for _ in range(a)]
    stickers.append(sticker)


# 해당 사이즈에 맞게 노트북에 들어가는지 확인하는 함수 # 붙였던걸 뗄 수는 없음
# tg 구역, 스티커 모양이 ㄱㅊ은지 판단
def judge_available(tg_area, sticker):
    A = len(sticker)
    B = len(sticker[0])

    for a in range(A):
        for b in range(B):
            if tg_area[a][b] == 1 and sticker[a][b] == 1:
                return False
    return True


# 스티커를 시계방향 90도 돌리는 함수
def rotate_sticker_90(sticker):
    A = len(sticker)
    B = len(sticker[0])

    a, b = B, A
    rotate_sticker = [[0] * b for _ in range(a)]

    for i in range(A):
        row = sticker[i]
        for j in range(B):
            numb = row[j]
            rotate_sticker[j][A - 1 - i] = numb

    return rotate_sticker


for idx in range(len(stickers)):

    sticker = stickers[idx]

    for _ in range(4):  # 0, 90, 180, 270

        is_fitted = False

        for cpi in range(I - len(sticker) + 1):
            for cpj in range(J - len(sticker[0]) + 1):

                cur_position = (cpi, cpj)
                tmp = [[0] * len(sticker[0]) for _ in range(len(sticker))]

                for k in range(len(sticker)):
                    for l in range(len(sticker[0])):
                        tmp[k][l] = labtop[k + cur_position[0]][l + cur_position[1]]
                '''
                print("---------------")
                for x in tmp:
                    print(x)
                print("::")
                for x in sticker:
                    print(x)
                print("---------------")
                '''
                is_fit = judge_available(tmp, sticker)
                # print(is_fit)

                if is_fit:
                    is_fitted = True
                    # 맞다면 이녀석을 붙인다
                    for k in range(len(sticker)):
                        for l in range(len(sticker[0])):
                            if labtop[k + cur_position[0]][l + cur_position[1]] != 1:
                                labtop[k + cur_position[0]][l + cur_position[1]] = sticker[k][l]
                    break
            if is_fitted:
                break
        if is_fitted:
            break
        sticker = rotate_sticker_90(sticker)  # 종료되지 못했으면 90도 돌린채로 진행

anw = 0
for i in range(I):
    for j in range(J):
        if labtop[i][j] == 1:
            anw +=1
print(anw)