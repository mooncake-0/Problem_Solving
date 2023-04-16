import sys
from heapq import *

input = sys.stdin.readline

ugly_nums = []

'''
생각이 좀 딸렸었는 듯
당연히 연계되어 나갔어야 하는 생각
순서대로 나열되게 하고, 순서대로 a, b, c 하나씩 늘려가면서 확인하고, 그것을 ugly_nums 에 넣는데, 순서대로 넣으니 맨 뒤에거로만 확인하면됨. 
>>> 그 와중에 Heap 을 통해 제일 작은 수 부터 정렬되게 나간다

'''

# 1500 개 돌리기
# 가장 먼저 해볼 수 있는 건 소인수 분해를 찾고, 2,3,5 밖에 없는지 확인하기
# 1500까지 채워야 해서 너무 오래걸림

# 두번째 생각할 수 있는 것
# 2^a * 3^b * 5^c 에서, abc 를 늘려나가는 것
# 늘리면서 ugly 숫자들을 채워주며, 중복을 제거 한다
# 단, 중복 체킹 할 때, in ugly 를 사용하면 O(N) 이기 때문에, 그냥 가장 큰값이였을 마지막 수와 비교해주면 된다
# 왜냐면 지금 ugly 는 순서대로 집어넣고 있기 때문
# 1500 개의 배열을 채워놓는다
def init_ugly():
    hq = [1]
    while len(ugly_nums) < 1500:
        # hq 에서 가장 작은 원소를 가져와서, 순서대로 넣어줄거임
        target = heappop(hq)
        # 그냥 이 떄 ugly 의 제일 최신거랑 같으면 안넣어주면 됨.
        # 왜냐면 heap 은 계속해서 최솟값을 주기 때문
        if ugly_nums and ugly_nums[-1] == target: continue

        # 넣어줘도 된다면
        ugly_nums.append(target)
        heappush(hq, target * 2)
        heappush(hq, target * 3)
        heappush(hq, target * 5)
    # print(ugly_nums)

def main():
    while True:
        tmp = int(input())
        if tmp == 0:
            break
        print(ugly_nums[tmp-1])


init_ugly()
main()
