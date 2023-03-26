import sys
from collections import defaultdict

sys.stdin = open("input_8933.txt")
input = sys.stdin.readline


def turn_dict(x):
    tmp = defaultdict(int)
    for k in x:
        tmp[k] += 1

    return tmp


# hashing 필요
# 뭐 괜찮게 진행하긴 했는데... 이걸로 13번은 못품.. (해봄..)
def pro2(length, dnas):
    lib = defaultdict(int)
    for i in range(len(dnas) - length):
        tbA = turn_dict(dnas[i:i + length])
        listA = []
        for k in tbA:
            listA.append(k + str(tbA[k]))
        listA.sort()
        lib[tuple(listA)] += 1

    max_cnt = -1
    for a in lib:
        max_cnt = max(max_cnt, lib[a])
    print(max_cnt)


# NAIVE
def pro1():
    length = int(input())
    dnas = input()
    lib = defaultdict()
    max_cnt = 0
    # O(6만)
    for i in range(len(dnas) - length):
        cnt = 0
        # print("1:", dnas[i:i+length])
        # O(3,600,000,000) > 36 억 ^_^ 심지어 답도 틀림 ㅋㅋ
        for j in range(i, len(dnas) - length):
            # 그 안에 O(*length**2)
            tbA = turn_dict(dnas[i:i + length])
            tbB = turn_dict(dnas[j:j + length])

            if tbA == tbB:
                cnt += 1
                # print("2:", dnas[j:j+length], "cnt: ", cnt)

        max_cnt = max(max_cnt, cnt)
    print(max_cnt)


def main():

    for TC in range(int(input())):
        k, dnas = map(str, input().strip().split())
        k = int(k)
        # pro1()
        pro2(k, dnas)


main()
