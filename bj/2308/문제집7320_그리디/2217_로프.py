import sys

sys.stdin =open("input_2217.txt")
input = sys.stdin.readline

N = int(input())  # N ~ 100,000

'''
최대 중량 구해보셈
900
1000
1100

1. 제일 큰 수는 집합에 포함된다
2. 하나씩 본다

# 명제 : 만약 얘가 낀 이후, 
# (그 중 제일 작은 수) * (꼈을 때의 cnt) > 지금까지 MAX 중량 

> 그리디 상, 내림차순이 말이 됨
> 무거운 것 부터 판단해야 무거운 무게에 대한 판단을 할 수 있는 것
> 하나씩 사용해서 넘기는게 아니라, 다같이 사용해서 넘기는걸 판단해야지... 당연하지
> 사실 하나하나 다해보는게 맞아 
> 맞는데 그리디인거임. > 지금 최대한 많은 로프를 사용해 보려는 가정인거고, 그래서 하나씩이 아니라 다 해보려는 거임.
> 몇 개의 로프를 사용하든 그 다음에 영향을 주지도 않음


'''


def pro1():
    max_l_rope = -1
    max_idx = -1
    ropes = []
    for i in range(N):
        rope = int(input())
        ropes.append(rope)
        if rope > max_l_rope:
            max_l_rope = rope
            max_idx = i

    cur_length = 1  # 선택된 갯수를 구한다
    cur_min = max_l_rope
    cur_max_weight = max_l_rope

    for i in range(len(ropes)):  # (cl, cm, cmw) = (2, 1000, 2000), (3, 1000, 3000), 5, 700, 3500
        if i == max_idx:
            continue
        tmp_min = min(cur_min, ropes[i])  # 제일 작은 수를 고른다

        if tmp_min * (cur_length + 1) > cur_max_weight:  # select 에 추가한다
            cur_length += 1
            cur_min = tmp_min
            cur_max_weight = cur_min * cur_length
    return cur_max_weight


# 내림차순으로 정렬 후. 하나씩 더하면서 들 수 있는 무게를 확인
# 마지막에 max 값 추출
# "많은 rope 를 사용할 수록 많이 들 수 있다" >> 무거운 걸 들 수 있는 rope 부터 판단
def pro2():
    ropes = [int(input()) for _ in range(N)]
    ropes.sort(reverse=True) # 오름차순 정렬 수행
    weights = []
    for i in range(len(ropes)):
        weights.append(ropes[i] * (i+1)) # 들 수 있는 모든 무게는 마지막 인자가 결정한다 # i+1 은 현재 갯수
    print(max(weights))


def main():
    # print(pro1())
    pro2()

main()