import sys
from heapq import *

# N 명의 스카우터가, M 명의 선수를 평가 (1<= n,m <= 10,000)
# sid ~ 100,000,000, pname 5자, score ~10
# sid list -> 400,000,000 : 400MB > Memory 부족

sys.stdin = open("input_40.txt")
input = sys.stdin.readline

# sum, avg 함수는 pq 에서 바로 뽑아낼 함수
# eval 과 clear 에 따라 sum, avg 에 대해 queue 들이 update 될 것이다.
# 일단 필요 PQ
sum_min_hq, sum_max_hq, avg_min_hq, avg_max_hq = [], [], [], []

# 일단 특정 선수들이, 그 sid 로부터 몇 점을 받았는지들이 있어야 함
# name -> (sid, score) 에 대한 map 작성 ( 바로바로 탐색을 위함)
# sid 가 새로 평가를 내리면, 덮어 씌워야 한다
player_records = dict()

# 또한 clear 를 위해 sid 가 어떤 선수들에게 내렸는지 확인할 수 있어야함
# 하지만 sid 는 1억까지 : 존재하는 sid 들만 해야한다 > map 써야할 듯
sid_evals = dict()


def eval(sid, pname, score):  # SID 가 PLAYER 에 대한 평가를 내린다
    #################### Base 정보 추가 로직

    sid = int(sid)
    score = int(score)
    if pname not in player_records:
        player_records[pname] = {sid: score}
    else:  # 있었으면 바꾸고, 없었으면 map 에 추가된다
        player_records[pname][sid] = score

    if sid not in sid_evals:
        sid_evals[sid] = {pname: score}
    else:
        sid_evals[sid][pname] = score

    #################### PQ 관리 로직
    # 해당 선수가 받은 모든 점수를 가지고와서 업데이트를 진행해준다
    records = player_records[pname]
    sum_ = 0
    for sid in records:
        sum_ += records[sid]
    avg_ = round(sum_ // len(records), 1)

    heappush(sum_min_hq, (sum_, pname))
    
def clear(sid):  # SID 의 모든 평가 정보 삭제
    pass


# flag == 1 총점 가장 높은 선수 // 그 다음은 사전순으로 느린 선수
# flag == 0 총점 가장 낮은 선수 // 그 다음은 사전순으로 빠른 선수
def sum(flag):
    pass


# flag == 1 평균 점수가 가장 높은 선수 // 그 다음은 사전순으로 느린 선수
# flag == 0 평균 점수가 가장 낮은 선수 // 그 다음은 사전순으로 빠른 선수
def avg(flag):
    pass


def main():
    N, M = map(int, input().split())
    pnames = list(map(str, input().strip().split()))
    q = int(input())
    for _ in range(q):
        cmd, *val = map(str, input().strip().split())
        if cmd == 'EVAL': eval(*val)
        if cmd == 'CLEAR': clear(*val)
        if cmd == 'SUM': sum(*val)
        if cmd == 'AVG': avg(*val)


main()
