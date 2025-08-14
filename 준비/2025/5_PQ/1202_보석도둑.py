
'''
실패해서 솔루션 본 문제!!
    정렬에 대한 감각과 HQ 를 중단 후 지속 사용하는 조금 아트한 계열의 문제였던 듯. 훌륭한 풀이
'''

import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
jewel_arr_idx = 0  # 뒤에서 사용할 iterator
bags = []
for _ in range(N):
    a, b = map(int, input().split())  # 무게, 가격
    jewels.append((a, b))
for _ in range(K):
    w = int(input())
    bags.append(w)

bags.sort()  # 가방도 무게 순대로 정렬
jewels.sort(key=lambda x: x[0])  # 쥬얼리도 무게 순대로 정렬

jewel_storage = []
anw = 0  # 가져갈 수 있는 최대 가격

for bag in bags:
    # 각 jewel 을 보면서, 현재 bag에서 가능하면 queue 에 넣어두고, 못 넣는 시점이 오면 이번 bag 는 여기까지! 한다
    # jewel 도 다 썼으면 이제 queue 에 그만 넣는다
    while jewel_arr_idx < N and bag >= jewels[jewel_arr_idx][0]:
        heapq.heappush(jewel_storage, -1 * jewels[jewel_arr_idx][1])
        jewel_arr_idx += 1  # 다음거 봐야지

    # 이번 가방이 쓸 녀석을 가져간다
    if jewel_storage:
        this_one = heapq.heappop(jewel_storage) * -1
        anw += this_one

print(anw)

'''
SOL1 - 
    HEAPIFY 해. 비싼 순서대로.
    하나씩 뽑아서 전체 돌려 O(logN) 
    그리고 그 안에서 그 비싼거 들 수 있는 가방을 O(N) 으로 돌면서 찾는다. (NlogN 정도, 2백 안넘을듯)
    들 수 있는 무게를 넘지 않으면서 그 차이가 가장 작은 것으로!

SOL2 - 
    어차피 보석의 HEAP looping 은 바뀌지 않을것이라 생각
    차라리 적합한 가방 찾는 과정을 for looping 에서 줄여보는 걸로
    정렬에 유리하므로, 이분 탐색으로 변경
    -> 사용한 가방 제거 때문에 이분 탐색은 어려움

SOL3 - 솔루션 봄..
    SOL2 같은 이유로 bags 는 유지하고, 오히려 보석을 hq 를 "그 때 넣을 수 있는 보석" 을 넣는 방식으로 바꿈
    정렬에 대한 감각과 HQ 를 중단 후 지속 사용하는 조금 아트한 계열의 문제였던 듯. 훌륭한 풀이

'''
'''
def binary_search(weight):
    st, end = 0, K - 1  # 마지막
    while st + 1 < end:
        mid = (st + end) // 2
        if bags[mid] - weight < 0:  # 현재 가방으로 weight 를 들 수 없음, bags 는 가볍게 정렬되어 있으므로, 더 무거운 가방을 찾아야 한다
            st = mid
        else:
            end = mid
    return end # 들 수 있는 가방 중 가장 적합한 가방 idx를


while hq:  # 다 고려는 해보는 것 (힙 자체를 줄일 수도 없을 것)
    _price, weight = heapq.heappop(hq)
    price = _price * -1

    decided_idx = -1
    for i in range(len(bags)):  # 무게를 넘지 않으면서 차이가 가장 적은 것
        if bags[i] == -1:
            continue
        if bags[i] - weight < 0:  # 들 수 없으면 안된다
            continue
        else:
            if bags[i] - weight <= min_diff:
                decided_idx = i
                min_diff = bags[i] - weight
    if decided_idx != -1:  # 들기로 결정
        bags[decided_idx] = -1
        sums += price

print(sums)
'''

## SOL3 - 정답 확인
#  오히려 heapq 를 바꿔야 했다. bags 를 돌면서, heapq 를 "넣을 수 있는 보석만 넣고 재활용" 하는 방식으로
#  heapq 의 장점을 좀 제대로 사용한 솔루션 -> 계속 넣으면서 대상들이 가져갈 것만 가져가도록
