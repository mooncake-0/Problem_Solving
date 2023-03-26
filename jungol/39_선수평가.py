import sys
from heapq import *

sys.stdin = open("input_39.txt")
input = sys.stdin.readline

s_num, p_num = map(int, input().split())
q = int(input())

# 각 sid 가 pid 에 대해서 score 에 대한 평가를 내린다
# 특정 sid 가 해당 pid 에게 내린 점수?
# 특정 pid 가 받은 모든 점수?


# 어쨌든 네 종류의 힙이 필요한건 맞다고 봄


s_max_heap, s_min_heap, a_max_heap, a_min_heap = [], [], [], []

# 서로 교차해서 저장해 놓는다.
pid_eval = dict()  # pid_eval = {pid : {sid: score} }

pid_cur_sum = dict()
pid_cur_avg = dict()

# p_num 에 대해서 모두 저장해야하는데..?
for i in range(1, p_num + 1):
    heappush(s_min_heap, (0, i))
    heappush(s_max_heap, (0, -i))
    heappush(a_min_heap, (0, i))
    heappush(a_max_heap, (0, -i))
    pid_cur_sum[i] = 0
    pid_cur_avg[i] = 0


def sync(pid):
    cur_pid_eval = pid_eval[pid]  # 현재 PID 의 모든 평가 dict 을 가져온다
    if cur_pid_eval:
        sum = 0

        for sid in cur_pid_eval:
            sum += cur_pid_eval[sid]

        avg = round(sum / len(cur_pid_eval), 0)

        pid_cur_sum[pid] = sum
        pid_cur_avg[pid] = avg

        heappush(s_min_heap, (sum, pid))
        heappush(s_max_heap, (-sum, -pid))
        heappush(a_min_heap, (avg, pid))
        heappush(a_max_heap, (-avg, -pid))

    else:  # 현재 PID 에 대한 평가가 없다 > 없음으로 최신화
        pid_cur_sum[pid] = 0
        pid_cur_avg[pid] = 0
        heappush(s_min_heap, (0, pid))
        heappush(s_max_heap, (0, -pid))
        heappush(a_min_heap, (0, pid))
        heappush(a_max_heap, (0, -pid))


def eval(sid, pid, score):
    ''' dict 관리 '''
    if pid in pid_eval:  # 수정이 필요하면 다 필요함 (동기화)
        pid_eval[pid][sid] = score  # 해당 선수에게 있는 해당 sid 의 평가를 바꿈
    else:
        pid_eval[pid] = dict({sid: score})

    ''' HEAP 들 관리'''
    # 업데이트 할 수 없음. 그냥 계속 넣는다
    # 현재 시점에서 해당 선수의 sum, avg 정보를 기준으로 heap 에 push 한다
    # 여기서 필요한게 pid_dict
    sync(pid)


# sid 의 모든 평가 정보를 삭제한다
def clear(sid):
    # 다관리해줘야함
    target_pid = []

    ''' 관리 list 들 '''
    for pid in pid_eval:  # O(N)
        if sid in pid_eval[pid]:  # O(1)
            target_pid.append(pid)  # 삭제 대상이였던 친구들에 대해 최신화를 해줘야 함
            del pid_eval[pid][sid]

    ''' player 에 대한 heap, list 최신화'''
    for x in target_pid:
        sync(x)


def sum(flag):
    if flag == 1:  # 총점이 가장 높은 선수의 번호, 같다면 번호 제일 큰놈
        pid = -1 * (s_max_heap[0][1])
        score = -1 * (s_max_heap[0][0])
        while pid_cur_sum[pid] != score:
            heappop(s_max_heap)
            pid = -1 * (s_max_heap[0][1])
            score = -1 * (s_max_heap[0][0])

    else:  # 총점이 가장 낮은 선수의 번호, 같다면 번호 제일 작은 놈
        pid = s_min_heap[0][1]
        score = s_min_heap[0][0]
        while pid_cur_sum[pid] != score:
            heappop(s_min_heap)
            pid = s_min_heap[0][1]
            score = s_min_heap[0][0]
    print(pid)


def avg(flag):
    if flag == 1:  # 평점이 가장 높은 선수의 번호
        pid = -1 * (a_max_heap[0][1])
        score = -1 * (a_max_heap[0][0])
        while pid_cur_avg[pid] != score:
            heappop(a_max_heap)
            pid = -1 * (a_max_heap[0][1])
            score = -1 * (a_max_heap[0][0])
    else:
        pid = a_min_heap[0][1]
        score = a_min_heap[0][0]
        while pid_cur_avg[pid] != score:
            heappop(a_min_heap)
            pid = a_min_heap[0][1]
            score = a_min_heap[0][0]
    print(pid)


def main():
    for _ in range(q):
        cmd, *val = map(str, input().strip().split())
        if cmd == 'EVAL': eval(*map(int, val))
        if cmd == 'CLEAR': clear(*map(int, val))
        if cmd == 'SUM': sum(*map(int, val))
        if cmd == 'AVG': avg(*map(int, val))


main()
