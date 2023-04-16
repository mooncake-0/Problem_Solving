'''
첫 행에 질의의 수 Q(1 ~ 200,000)가 주어진다.
다음 Q개의 행에 명령이 주어진다.
id: 1~100,000 개 있음
# 쓰였는지 여부를 파악해보려면, [] 가 있으면 되는데, 4* 100,000개의 integer = 400,000 > 400Mb > 메모리 초과날것.
Q개의 명령 중에 3, 4에 대한 결과를 행으로 구분하여 출력한다.

>>> heap updating 에 대한 확인
>>> 특정 값을 계속 주시해야 하는 것이면 Heap 을 의심해볼 필요가 있음
'''

# 그냥 max_pq, min_pq 하면서 update 다스리기 해보는 것
import sys
from heapq import *

sys.stdin = open("input_36.txt")
input = sys.stdin.readline

max_hq = []  # (id, value)가 최대 Heap 들어간다. (-value, -id) 로 들어가서 우선순위가 최대 value, 그 다음이 최대 id 임을 명시한다
min_hq = []  # (id, value)가 최소 Heap 으로 들어간다. (value, id) 로 들어가서 우선순위가 최소 value, 그 다음이 최소 id 임을 명시한다

flags = [0] * 100001  # 1~ 100000 까지의 최신 상태를 기록한다, value 는 1 부터 이므로, 존재하지 않아야 되는 id 는 0 이다


def addOrUpdate(id, value):  # 해당 id, value 로 추가 ,업데이트 한다
    # 그냥 넣는다, 그리고 flag 기록한다
    flags[id] = value
    heappush(max_hq, (-value, -id))
    heappush(min_hq, (value, id))


def delete(id):  # 있으면 삭제 없으면 무시
    flags[id] = 0  # 힙 안에 들어있는 id 의 값은 유효하지 않음을 체킹할 수 있다.


def printMinVal():  # 최소 value 출력, 그러한 값이 여러개라면 가장 작은 id 미존재시 -1
    # MIN HEAP 에서
    # ROOT 값이 답이긴 한데, 현재 flags 와 체킹을 해줘야 한다
    min_val = -1
    while min_hq:
        anw = min_hq[0]
        anw_val = anw[0]
        anw_id = anw[1]
        if flags[anw_id] == anw_val:  # 얘가 맞다면
            min_val = anw_id
            break
        # 지나간다면 얘 버리면 됨.
        heappop(min_hq)

    print(min_val)


def printMaxVal():  # 최대 value 출력, 그러한 값이 여러개라면 가장 큰 id 미존재시 -1
    max_val = -1
    while max_hq:
        anw = max_hq[0]
        anw_val = -1 * anw[0]
        anw_id = -1 * anw[1]
        if flags[anw_id] == anw_val:  # 얘가 맞다면
            max_val = anw_id
            break
        # 지나간다면 얘 버리면 됨.
        heappop(max_hq)

    print(max_val)


def main():
    query = int(input())
    for _ in range(query):
        cmd, *val = map(int, input().split())
        if cmd == 1: addOrUpdate(*val)
        if cmd == 2: delete(*val)
        if cmd == 3: printMinVal()
        if cmd == 4: printMaxVal()


main()
