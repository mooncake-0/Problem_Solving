import sys
from collections import deque


def find_max(risk_q):
    max = risk_q[0][1]
    for i in range(len(risk_q)):
        if max < risk_q[i][1]:
            max = risk_q[i][1]
    return max


sys.stdin = open("input_6.txt")
T = int(input())

for _ in range(1, T + 1):
    n, m = map(int, input().split())
    # pos 에 대한 tuple 값을 만들어서 risks 에 list 화시킨다
    # for 문은 이해 됐는데, 맨 앞에 (pos, val) for 부분이 좀 이해가 안됨. 이게 list 로 만들라는 표현?
    risks = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
    risk_q = deque(risks)
    ''' 내 풀이 (위의 함수 포함) 
    seq = []
    while len(risk_q) > 0:
        if risk_q[0][1] < find_max(risk_q):
            risk_q.append(risk_q.popleft())
        else:  # 자기가 가장 큰 것임
            seq.append(risk_q.popleft())
    for i in range(len(seq)):
        if seq[i] == risks[m]:
            print(str(i + 1))
            break
    
    '''
    # 강사님 풀이
    cnt = 0
    while True:
        cur = risk_q.popleft() # (0,60) 이런 식으로 나옴
        if any(cur[1] < x[1] for x in risk_q): # any 라는 제공 함수 사용. iter 를 돌려서 조건 확인하는 함수 (lamda 같은 것으로, risk_q 에 있는 것을 x 로 접근 해서 판별식 판단)
            risk_q.append(cur)
        else:
            cnt += 1
            if cur[0] == m:
                break
    print(cnt)

