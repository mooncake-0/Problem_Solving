import sys
from heapq import *

input = sys.stdin.readline

'''
포인트
  - 탐색해야 하는 조건이 발생하니까 어떤 변화가 생기는지 잘 판단해야 함
  - 변화 1) 일단 main_HEAP 을 계속 건드리면 안되었다. 3,4 의 동작이 불필요한거 빼내는건 상관 없는데, 뒤에 후속 작업을 위해 건드리면 안되었다. 
        2) 중복으로 들어가는 값들이 있을 때 걸러줄 필요가 있다. (현재 값 == 이전에 들어갔던 값) 이면, 현재 node 가 오기 전에 녀석들이 횟수로 cnt 될 수 있다. 
        3) -> smp = [] 로 만들었고, not in 을 하며 중복된 id 들을 걸러주는 작업을 해줌 -- TO Error  발생
        4) -> set 으로 해서 not in 을 굳이 거치지 않고 집합으로 O(1) 에 처리될 수 있도록 시도 -- 이거도 안되면 copy 가 문제임이 자명
        5) https://velog.io/@emplam27/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B9%8A%EC%9D%80%EB%B3%B5%EC%82%AC%EB%8A%94-deepcopy%EA%B0%80-%EB%B9%A0%EB%A5%BC%EA%B9%8C-slicing%EC%9D%B4-%EB%B9%A0%EB%A5%BC%EA%B9%8C
            -> 를 참고해보면, deepcopy 보다 slicing 이 훨씬 빠른 모습을 확인할 수 있다. copy 도 비슷할 것 같아서  [:] 로 리스트 복사를 진행해봤다. 
        6) ㅋㅋㅋ 계속 시간 초과난다. 
        7) 어쨌든 새로운 list 생성 O(N) 이 문제임 > 그냥 그거 없이 해야함 > 단순하게 빼줬던 것 (set) 들을 다시 더해주고 HEAPIFY 해주는 방향으로 해줬다.
        8) 일일이 list append 한 다음에 HEAPIFY 를 하거나, 하나씩 HEAPPUSH 를 하거나 둘 중 하나 해주면 되는데, 둘다 비슷한 시간 복잡도 인듯.
        9) 이래도 런타임 에러가 남
        10) 8번 가정이 존나 틀렸음 HEAPIFY 는 O(N) 이;고 / HEAP PUSH 는 O(logN) 임. 3LogN vs O(N) 인데, 당연히 전자가 훨씬 빠름..
        11) HEAPPUSH 하니까 통과 함... 생각보다 간단했던 문제. (3번과, 8번만 그냥 하면 되었었..) 

'''

max_hq = []
min_hq = []

flags = [0] * 100001


def addOrUpdate(id, value):  # 해당 id, value 로 추가 ,업데이트 한다
    # 그냥 넣는다, 그리고 flag 기록한다
    if flags[id] != value:  # 같은건 넣어주지 않는 간단한 조건 정도는 ..
        flags[id] = value
        heappush(max_hq, (-value, -id))
        heappush(min_hq, (value, id))


def delete(id):  # 있으면 삭제 없으면 무시
    flags[id] = 0  # 힙 안에 들어있는 id 의 값은 유효하지 않음을 체킹할 수 있다.


def printMinVal():  # 최소 value 출력, 그러한 값이 여러개라면 가장 작은 id // 순서대로 세웠을 경우 세번째 위치를 출력한다
    smp = set()
    val = -1  # 3개가 되기 전이거나 비어 있으면 -1 출력

    while min_hq:
        anw = min_hq[0]
        anw_id = anw[1]
        anw_val = anw[0]
        if flags[anw_id] == anw_val:
            smp.add(anw_id)
        if len(smp) == 3:  # 하고 나왔는데 2 임
            val = anw_id
            break
        heappop(min_hq)

    # 빠진 애들을 다시 더해준다
    for id in smp:
        heappush(min_hq, (flags[id], id))

    print(val)


def printMaxVal():  # 최대 value 출력, 그러한 값이 여러개라면 가장 큰 id 미존재시 -1
    smp = set()
    val = -1  # 3개가 되기 전이거나 비어 있으면 -1 출력
    while max_hq:
        anw = max_hq[0]
        anw_id = -1 * anw[1]
        anw_val = -1 * anw[0]
        if flags[anw_id] == anw_val:
            smp.add(anw_id)
        if len(smp) == 3:  # 하고 나왔는데 2 임
            val = anw_id
            break
        heappop(max_hq)

    # 빠진 애들을 다시 더해준다 (차피 MAX 가 O(3))
    # heap
    for id in smp:
        heappush(max_hq, (-flags[id], -id))

    print(val)


def main():
    query = int(input())
    for _ in range(query):
        cmd, *val = map(int, input().split())
        if cmd == 1: addOrUpdate(*val)
        if cmd == 2: delete(*val)
        if cmd == 3: printMinVal()
        if cmd == 4: printMaxVal()


main()
