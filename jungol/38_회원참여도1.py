import sys
from heapq import *

'''
음.. 37번이 더 어려웠던 듯. 크게 생각할건 없고, update 에서 Heap 을 사용할 때에 대한 연습 
'''

input = sys.stdin.readline
# 회원 ID 0~ 100000
# 명령 100,000

status = [0] * 100000  # 현 상태를 저장한다
max_hq = []  # (-freq, -id) 순서로 저장되어, 최대 freq 다음 최대 ID 이다
min_hq = []  # (freq id) 순서로 저장되어, 최소 freq 다음 최소 ID 이다
sums = 0
valid_cnt = 0

from_3 = False


# 중복입력은 제외된다
def add(id, freq):
    global sums, valid_cnt
    valid_cnt += 1
    sums += freq
    status[id] = freq
    heappush(min_hq, (freq, id))
    heappush(max_hq, (-freq, -id))


def removeLast():
    global sums, valid_cnt, from_3
    while min_hq:
        anw = min_hq[0]
        # anw = heappop(min_hq)
        anw_freq = anw[0]
        anw_id = anw[1]
        if status[anw_id] == anw_freq:
            if not from_3:
                print(anw_id)
                heappop(min_hq)
                sums -= anw_freq
                status[anw_id] = 0
                valid_cnt -= 1
                break
            else:
                return anw_id
        heappop(min_hq)  # 어쨌든 POP 되는 애들은 다 제거되는 것
    return -1


def removeFirst():
    global sums, valid_cnt, from_3
    while max_hq:
        anw = max_hq[0]
        anw_freq = -1 * anw[0]
        anw_id = -1 * anw[1]
        if status[anw_id] == anw_freq:
            if not from_3:
                print(anw_id)
                heappop(max_hq)
                sums -= anw_freq
                status[anw_id] = 0
                valid_cnt -= 1
                break
            else:
                return anw_id
        heappop(max_hq)
    return -1


# 참여도 가장 높은 사람과 낮은 사람은 제외한다
def allFreq():
    global from_3
    from_3 = True
    if valid_cnt <= 2:
        print(0)
    else:  # 위에 대상들을 뽑아야 한다
        biggest_freq_id = removeFirst()
        smallest_freq_id = removeLast()
        if biggest_freq_id == -1 or smallest_freq_id == -1:
            from_3 = False
            return
        print(sums - status[biggest_freq_id] - status[smallest_freq_id])
    from_3 = False


#  현재 list
# 0: 0
# 20 : 7
# 99999 : 15 \
# 3 첫출력 > 0, 15 제외 > 7 출력
# 1> 0 이 빠진다
# 2 > 99999 가 빠진다
# 3 > 하나밖에 없다.


def main():
    N, cmds = map(int, input().split())
    for _ in range(cmds):
        mode, *val = map(int, input().split())
        if mode == 0: add(*val)
        if mode == 1: removeLast()
        if mode == 2: removeFirst()
        if mode == 3: allFreq()


main()
