from heapq import *

NODE_CNT = 6
NODE_MAP = [  # 가중치가 0 인 상황은 없다라는 가정 하에 다음과 같이 설계
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 5, 1, 0, 0],
    [0, 2, 0, 3, 2, 0, 0],
    [0, 5, 3, 0, 3, 1, 5],
    [0, 1, 2, 3, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 2],
    [0, 0, 0, 5, 0, 2, 0]
]

# 무한대? 란 표현을 뺀 이유 >> 아니 거리가 갈 수 없음을 무한대라고 보는게 좀 이상함
# 조건에서 걸러지게 하기 위한것이였으므로, 차라리 연결되어 있지 않다라는 표현을 해주는게 더 낫다라는 생각
def main():
    TG = 1
    anw_list = [-2] + [-1] * (NODE_CNT)  # -1 은 최신화가 안됐다는 뜻
    hq = []

    # 자기자신까지의 거리는 0 이므로, 아래와 같이 초기화한다
    heappush(hq, (0, TG))  # (TG 노드로부터 해당 노드까지의 최소 거리, 노드) # 노드가 앞에 와야 계속 최저 위주로 살피기 때문이다
    anw_list[TG] = 0

    while hq:

        # 해당 노드까지의 판단해본 거리를 말한다
        dist_of_tg_to_cur_node, cur_node = heappop(hq)

        '''
        판단
        1) 판단해보자고 나온 거리가, 지금 저장된 거리보다 작은지?
        2) 현재 해당 노드까지의 거리를 판단한 적이 있는지? - 이건 일단 해보지 말아보자
        '''
        # 현재 1-> 3 은 3이였음
        # 근데 4에서 3 가는게 있어서 5,3 이 들어왔음 (왜냐하면 이 거리는 1->4->3 이 5라고 판단한 것이기 때문)
        # 그럼 저장된 값보다 큰게 왔으니 버린 다음에 바로 다음꺼 뽑으면 됨
        # 참고로 anw_list = -1 의 값이라는건, 현재 한번도 들어오지 않았다는 뜻임
        # 이 때, -1 이면 꼭 넣고 판단해야 하지만, -1이 아니라고 해서 판단하면 안되는건 아니라 생각
        # 따라서, -1 일 경우에 대한 경우 말고, 1에 대한 판단만 하면 됨

        if dist_of_tg_to_cur_node > anw_list[cur_node]:  # 같으면 봐야함. 바로 전에 최신화된 값을 봐야하는 상황일 경우가 많기 때문
            continue

        # 다익스트라 할 때 anw_list 에 대한 최신화는 끝냈을테니, 이제 다시 다음 node 들을 확인하며 돌려야 한다
        tmp = NODE_MAP[cur_node]
        for idx in range(1, NODE_CNT + 1):
            if tmp[idx] != 0:
                if anw_list[idx] == -1 or dist_of_tg_to_cur_node + tmp[idx] < anw_list[idx]: # 더 작은 경로라면 최신화해주고 HEAP 에 넣는다
                    anw_list[idx] = dist_of_tg_to_cur_node + tmp[idx]
                    heappush(hq, (anw_list[idx], idx))

    print(anw_list)

main()
