import sys
from heapq import *

sys.stdin = open("input_1753.txt")
input = sys.stdin.readline

NODE_CNT, PATHS = map(int, input().split())
TG = int(input())
NODES = [[] for _ in range(NODE_CNT + 1)]

for _ in range(PATHS):
    # NODES 에는 해당 번호와 연결된 가중치가 tuple 로 저장된다
    a,b,c = map(int, input().split())
    # 양방향으로 저장해준다 (차피 중복 경로는 거를 것이다)
    NODES[a].append((b,c))

''' 기본 전역 SU 완료 '''

def pro1():
    hq = []
    heappush(hq, (0, TG)) # TG NODE 부터의 거리를 우선순위로 PQ 에 저장

    anw_list = [-2] + [-1] * (NODE_CNT)
    anw_list[TG] = 0

    while hq:
        # 판단해보고자 하는 NODE 까지의 거리
        distance_root_to_cur, cur_node = heappop(hq)

        '''
        cur_node 에 대해 판단한다는건, 이미 anw_list 에는 이미 특정 값이 저장되어 있을 것이다
        해당 로직 아래에서 판단을 할 때, anw_list 값을 바꿀 녀석들을 기준으로 hq 에 넣는다
        
        하지만 hq 에는 거리가 가까운 녀석들이 앞에 배치되는 상태로 들어가게 될 것이다
        따라서 순서대로 들어가는 것은 아니지만, 가까운 녀석들을 우선적으로 보게된다는 보장을 해준다
        
        그리고 판단할 때도 제일 가까운 녀석들임을 판단한 다음에 hq 에 넣어주기 때문에,
        일반 Q 보다 들어가게 될 값이 훨씬 적다.
        일반 Q 를 사용하면 최저 값을 먼저 넣어준다는 보장이 없으므로, 
        아래 a + b < c 로직을 통과해서 들어가게 되는 NODE 값이 훨씬 많게 된다
        > HQ 를 사용하여 최저값을 주시하고 있는 이유이다. 
        > 그리고 그 NODE 의 최저값이 anw_list 로 SU 되어 있다면, 해당 NODE 에 대한 판단 값은 PQ에
        > 안들어가기 시작할 것이므로, 모든 NODE 를 돌 수 있게 된다
        '''
        if distance_root_to_cur > anw_list[cur_node]:
            '''
            1) 같을 경우 : 이 로직은 여기에 들어있는 값이 현재 저장된 값일 경우, 이 쪽으로 이동을 해서 이제 다음 번으로 넘어가 줘야 한다 > 이 걸 위해서 하기 로직이 존재
            2) 해당 case : 하지만 판단을 할 때 더 큰 값이 들어가 있을 수도 있다 (anw_list 값이 클때 먼저 들어갔는데, 판단값이 커서 hq 라서 뒤로 밀릴 수 있기 때문)
            그런 값들에 대해서는 판단을 할 필요 없이 다음 NODE 를 꺼내줘야 한다
            3) 오른쪽이 더 큰 case : 만약 더 작은 값이 들어올 경우, 판단을 해줘야 겠지만, 이 case 는 들어올리가 없을 것으로 추정
            > 그 이유 : 더 작으면 anw_list[distance_node] 값이 최적화되는 로직이고, 이 값이 hq 에 들어가게 된다
            > 그러므로 더 작은 값은 이미 anw_list[cur_node] 에 저장되어있을 것이기 때문에, 더 최적화된 값을 판단하고 있을리가 없다
            '''
            continue

        # 안들어옴을 확인할 수 있다
        if distance_root_to_cur < anw_list[cur_node]:
            print("Oh?")

        for dest_node, distance_cur_to_dest in NODES[cur_node]:
            # 초기화되지 않은 거리값이거나 or 다익스트라 알고리즘에 걸러지는 값일 경우
            if anw_list[dest_node] == -1 or distance_root_to_cur + distance_cur_to_dest < anw_list[dest_node]:
                anw_list[dest_node] = distance_root_to_cur + distance_cur_to_dest
                heappush(hq, (anw_list[dest_node], dest_node))

    for i in range(1, NODE_CNT+1):
        if anw_list[i] == -1:
            print("INF")
            continue
        print(anw_list[i])

def main():
    pro1()

main()
