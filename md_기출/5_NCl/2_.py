import sys

sys.stdin = open("input_2.txt")
input = sys.stdin.readline


def conv_to_set(numb):
    ret = set()
    for i in str(numb):
        ret.add(i)
    return ret


def sol(A):
    max_val = 0
    for i in range(len(A)):
        cnt = 1
        judge = conv_to_set(A[i])
        if len(judge) > 2:
            continue
        for j in range(i + 1, len(A)):  # 하나씩 추가하면서 판단한다
            adder = conv_to_set(A[j])
            judge.update(adder)  # 판단 후
            if len(judge) > 2:  # 두개가 넘어가면 종료한다
                break
            cnt += 1
        max_val = max(max_val, cnt)
    return max_val


A = list(map(int, input().split()))
print(sol(A))
