import sys

sys.stdin = open("input_9466.txt")
input = sys.stdin.readline

'''
포인트
    - 반례 찾아서 알아서 잘 해결함
    - 일단 근데 DFS 로 풀었나(?) 에 대한 의구심이 있음. 풀이를 확인해볼 필요가 있을 듯
    - 시간 초과 나서 list > dict 으로 줄여서 탐색 시간 줄인거 잘 한듯
    - 먼가 각각 상황을 해결하려고 코드들을 추가하는 짓을 했는데.. 그게 맞다보니 좀 찝찝한듯
'''

def judge_unchosen(index):
    global nums
    # table = [index]
    table = dict()
    global_index =0
    table[index] = global_index
    global_index +=1

    while True:
        # print(nums, table)
        points_to = nums[index]
        nums[index] = -1  # 얘에 대한 판단이 종료됨

        # 두 상황 중 하나가 될 때까지 계속 돌리는 것
        # 자기 자신을 가르키게 된다면
        if points_to == index:
            # 자신을 제외한 모든 애들이 다 unchosen 이다
            return len(table) - 1

        if points_to in table:
            return table[points_to]
        # for k in range(len(table)):
        #     if table[k] == points_to:  # 내가 가르키고 있는 애와 같은 애가 등장 > Loop 종료
        #         return k  # k 개가 unchosen 이다

        if nums[points_to] == -1:
            # 지금까지 있던 모두가 unchosen 이다
            return len(table)

        table[points_to] = global_index
        global_index+=1
        # table.append(points_to)
        index = points_to  # 그 다음 값으로 넘김


def pro1():
    global nums
    unchosen_cnt = 0
    #[1,3,1]
    for i in range(1, N + 1):
        # print("idx: ", i, unchosen_cnt)

        if nums[i] == -1:
            # 판단 끝난 친구
            continue

        if nums[nums[i]] == -1: # 판단이 끝난 친구를 가르키면
            unchosen_cnt += 1
            nums[i] = -1

        else:
            unchosen_cnt += judge_unchosen(i)

    return unchosen_cnt


# N: 2~ 100000
def main():
    global N, nums
    TC = int(input())
    for _ in range(TC):
        N = int(input())
        nums = [0] + list(map(int, input().split()))
        print(pro1())


main()
