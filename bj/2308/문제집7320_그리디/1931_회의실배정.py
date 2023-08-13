import sys
from heapq import *


'''
첫번째 풀이 - dict 활용한거
# mn = 1
# mx = 2^31-1 이였으면
# 벌써 O(10000000000000) 임.
# 절대 안되는 방법. 

두번째 - 같은 시간에 대한 회의 처리 
>> 현재 회의시간이 1~5 였는데, 6,6 이 들어왔으면, 1~6 이되는거래
>> ㄴㄴ 말장난은 아닌듯
>> 이게 문제임 >> 회의 시간이 4~7 이 잡혔는데,
>> 이전에 (6,6) 이 된다고 처리하는게 문제임
******>> 4~7 하는중에 6이 들어올 수가 없음 *******
>> 그래서 6,6 을 그냥 넘겨버리면 안됨
>> ~6 으로 end time 을 잡아서, 4~7 이 가용될 수 없는 회의임을 인지시켜야 한다
>> 나처럼 6,6 을 위처럼 그냥 같은 시간 처리해버리면.. 위에 상황을 허용하는 것

>> 근데 애초에 회의 같은 시간 처리가 좀 애반듯.. 

'''

sys.stdin = open("input_1931.txt")
input = sys.stdin.readline

N = int(input())
hq =[]

for _ in range(N):
    a, b = map(int, input().split())
    heappush(hq, (b,a))


s = -1
e = -1
cnt = 0
while hq:
    meeting = heappop(hq) # (4, 1)
    print(meeting[::-1])
    print("CURRENT",s, e)
    if meeting[0] == meeting[1]:
    #    e = meeting[0]
       cnt +=1
       continue
    if s == e and e== -1:
        s = meeting[1]
        e = meeting[0]
        cnt += 1
        continue

    # 가령, 현재 회의 잡힌 시간이 3~5 라 하자
    # 그럼 그 다음으로 주어질 수 있는 건 무조건 5 이후에 끝나는 회의들 (1,2,1,3 이런거 불가능) : HEAP 을 사용했기 때문
    # 5시에 끝나도 4~5 이런거 불가능
    # 가능 CASE 1 : 1~5 5가 동일 (안됨)
    # 가능 CASE 2 : 4~6 하나만 낑김 (안됨)
    # 가능 CASE 3 : 5~6 둘다 밖 (이것만 됨) s 는 그대로고, e 만 바뀐다
    # 1~ 8
    if meeting[1] >= e and meeting[0] > e:
        e = meeting[0]
        cnt += 1
        continue
print(cnt)

