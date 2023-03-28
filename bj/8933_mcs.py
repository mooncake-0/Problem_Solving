import sys
from collections import defaultdict

input = sys.stdin.readline

'''
포인트 
- SET 을 쓰는 문제는 아니였던 것 같음
- 고정 해싱에 대해서 생각할 수 있었으면 좋았을 듯!
'''

# 부족함..
# SET 을 뭔가 활용해야 할 것 같은데 ..
# SET 과 dict 는 탐색이 O(1) 이다
# 아이디어가 크게 다르지 않음
# 어쨌든 해싱을 지독하리만큼 쓰는 것
# ACGT 라는 Map 을 먼저 만들어 놓으면, 굳이 tmp 를 생성하고, 그 결과적으로 만들걸 sorting 하면서 까지 Order 를 낭비할 필요 없음
# 지금 완성된 형태에서 본인을 안세는 것 같음
def pro3(length, dnas):

    lib = {"A": 0, "C": 0, "T": 0, "G": 0}  # 고정된 value 내에서 탐색한다면, 이런 형태의 해싱을 한번 정도 생각해보면 좋을듯
    tmp = defaultdict(int)
    for i in range(len(dnas)):
        lib[dnas[i]] += 1

        if i >= length-1:
            lib[dnas[i-length]] -= 1
            #  여기까지 하면, 현재 length 길이의 ACTG 배열 횟수가 lib 에 저장되어 있는 상태
            #  이걸 쭉 앞으로 가려는 상태임. 뒤에 애들은 계속 빠질 것이고
            #  그 때의 lib 상태를 저장할텐데, lib의 모습이 그대로이므로, values 만 활용해서 저장해도 된다.
            tmp[tuple(lib.values())] += 1

    print(max(tmp.values()))

# O(600)
def turn_dict(x):
    tmp = defaultdict(int)
    for k in x:
        tmp[k] += 1

    return tmp


# hashing 필요
# 뭐 괜찮게 진행하긴 했는데... 이걸로 13번은 못품.. (해봄..)
# 60000 * (3N= 1800) 정도로, 1억이 살짝 넘음
# 통과할 수도 있지만, 못 통과할 수도 있는 수준임 (안에 +N 이 너무 많음)
def pro2(length, dnas):  # len = 600 //  W = 60,000
    lib = defaultdict(int)

    # O(60,000)
    for i in range(len(dnas) - length):
        tbA = turn_dict(dnas[i:i + length])
        listA = []
        # O(+len)
        for k in tbA:
            listA.append(k + str(tbA[k]))
        # O(+len)
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
        # pro2(k, dnas)
        pro3(k, dnas)
    # k = int(input())
    # dnas = input().strip()
    # pro3(k,dnas)


main()
