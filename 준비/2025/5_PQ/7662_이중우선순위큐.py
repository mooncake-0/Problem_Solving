import sys, heapq

input = sys.stdin.readline

'''
믿음으로 가는겨~
'''

# I 는 뒤에 숫자를 넣는다
# D 1은 최댓값 삭제, D -1 은 최솟값 삭제..?
# 그냥 HQ 두개 제어하는거 아님? - ㄴㄴ 삭제할 때 동기화가 포인트

def sol1(k):
    max_heap = []
    min_heap = []
    validator = []
    validator_idx = 0
    for _ in range(k):
        cmd, numb = input().split()
        numb = int(numb)
        if cmd == "I":
            validator.append(True)
            heapq.heappush(min_heap, (numb, validator_idx))
            heapq.heappush(max_heap, (-1 * numb, validator_idx))
            validator_idx += 1
        if cmd == "D":
            if numb == -1:  # 최솟값 삭제
                # heap 에 존재한다
                # valid 한 녀석이면 녀석을 버리고 종료하면 된다. 그리고 idx False 표시를 한다
                # valid 하지 않을 경우 버리기만 하고 다시하면 된다.
                while min_heap:
                    val, idx = heapq.heappop(min_heap)
                    if validator[idx]:
                        validator[idx] = False
                        break
            else:
                while max_heap:
                    _val, idx = heapq.heappop(max_heap)
                    if validator[idx]:
                        validator[idx] = False
                        break
        # print("max_heap :: ", max_heap)
        # print("min_heap :: ", min_heap)
        # print("validator :: ", validator)
    # 이 녀석이 마지막 남은 녀석일 수도 있어서, 뽑아버리면 안된다.
    # peek 를 하고 valid 하면 값을 출력하는 방식으로 가야 한다. valid 하지 않을경우는 버려도 된다.
    is_empty = True
    while max_heap:
        if validator[max_heap[0][1]]:  # valid 할 경우
            is_empty = False
            print(max_heap[0][0] * -1, end=" ")
            break
        else:
            heapq.heappop(max_heap)
    while min_heap:
        if validator[min_heap[0][1]]:
            is_empty = False
            print(min_heap[0][0])
            break
        else:
            heapq.heappop(min_heap)
    if is_empty:
        print("EMPTY")


TC = int(input())

for _ in range(TC):
    k = int(input())
    sol1(k)
