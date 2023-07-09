import sys

sys.stdin = open("input_3.txt")
input = sys.stdin.readline


def alpha_to_idx(alphabet):
    return ord(alphabet) - 64


def judge_set(row):
    cnt = 0

    for idx in range(2, len(row) - 3):
        if idx == 3 or idx == 5 or idx == 7:  # 통로 제외
            continue
        tmp = row[idx:idx + 4] # 잠깐 조각 확인
        if sum(tmp) != 0: # 앉은 자리가 있으면 무시
            continue
        else: # 다 비어있으면 바로 착석
            cnt += 1
            for i in range(idx, idx + 4):
                row[i] = 1

    return cnt


# N 1 ~ 50
def solution(N, S):
    global seats
    seats = [[0] * 11 for _ in range(N + 1)]
    taken = []
    if S:
        taken = S.split(" ")

    ''' 예약 좌석 배정 '''
    for resv in taken:
        i = int(resv[0:len(resv)-1])
        chr = resv[len(resv)-1]
        if chr =="J":
            chr = "I"
        elif chr == "K":
            chr = "J"
        j = int(alpha_to_idx(chr))
        seats[i][j] = 1

    ''' I 당 max family 반환 '''
    anw = 0
    for idxs in range(1, len(seats)):
        anw += judge_set(seats[idxs])
    return anw


N = int(input())
S = input().strip()
print(solution(N, S))
