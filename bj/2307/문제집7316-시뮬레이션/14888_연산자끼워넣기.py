import sys

'''
s 10:55
e 11:30
- 난 좀 복잡한 과정을 거침
- 10! 을 수행시킨 다음에 중복을 제거함 - 사실상 틀린거임. 왜냐면 시간제한 좀만 줄였어도 틀렸을 것임 -굳이 set 을 사용해서 메모리도 더 잡음
- 하지만 10!/ 중복  만큼의 계산과정이 들어오는게 더 들음 - 이걸로 시간제한 걸게 했으면 틀렸을 것임
- pro2 풀이가 정말 좋음
- DFS 로 모든 경우의 수를 고려하게끔 만들 수 있다 - pro2() - 백트래킹과 DFS 의 적용을 잘 활용함
- BFS 의 백트래킹도 공부해볼 필요가 있음
'''

sys.stdin = open("input_14888.txt")
input = sys.stdin.readline

N = int(input())  # N = 11
nums = list(map(int, input().split()))  #
cnts = list(map(int, input().split()))  # + - * / 갯수 # 연사자 MAX 갯수는 10인듯
cnt_index_list = []

for i in range(len(cnts)):
    if cnts[i] != 0:
        for j in range(cnts[i]):
            cnt_index_list.append(i)


# + - * /
# 0 1 2 3 순서대로
# str 조합으로 들어가게 되고
# set 에 묶어서 중복인것들을 뺄 수 있다

def permutation(selected):
    global total_perm
    if len(selected) == N - 1:
        tmp = ""
        for x in selected:
            tmp += str(cnt_index_list[x])
        total_perm.add(tmp)
    else:
        for i in range(len(cnt_index_list)):
            if i not in selected:
                selected.append(i)
                permutation(selected)
                selected.pop()


def dfs(depth, current_anw, plus_left, minus_left, times_left, div_left):
    global max_val_2, min_val_2
    if depth == N:  # N-1 의 연산이 완료되었다면 (연산자 N-1 개)
        max_val_2 = max(max_val_2, current_anw)
        min_val_2 = min(min_val_2, current_anw)
    else:  # depth 번째 연산을 의미
        if plus_left:  # 0 이 아니면 들어간다
            # plus 를 먼저 수행하고 나와도, plus_left = 2 이다. 왜냐하면 int는 call_by_value 이기 때문이다 (자료구조는  value 이므로 백트래킹을 따로 해야함)
            # + 의 갯수를 가지고 빼기 때문에, 중복도 자동으로 제거됨... ㄷㄷ
            dfs(depth + 1, current_anw + nums[depth], plus_left - 1, minus_left, times_left, div_left)
        if minus_left:  # 그래서 위에거 dfs 다 끝나고 들어오면, 이번엔 - 부터 해보는거다.
            dfs(depth + 1, current_anw - nums[depth], plus_left, minus_left - 1, times_left, div_left)
        if times_left:
            dfs(depth + 1, current_anw * nums[depth], plus_left, minus_left, times_left - 1, div_left)
        if div_left:
            re_ = False
            if current_anw < 0:
                current_anw *= -1
                re_ = True
            current_anw //= nums[depth]
            if re_:
                current_anw *= -1
            dfs(depth + 1, current_anw, plus_left, minus_left, times_left, div_left - 1)


# [skadmltls] 님의 풀이 클론
# 너무 좋은 방식
def pro2():
    global max_val_2, min_val_2
    max_val_2 = -1000000000
    min_val_2 = 1000000000
    dfs(1, nums[0], cnts[0], cnts[1], cnts[2], cnts[3])
    print(max_val_2)
    print(min_val_2)


# 내풀이
# 개 ㅈ망 풀이
def pro1():
    global total_perm
    # 어쨌든 1 2 3 4 5 # 이렇게 와 있으면 연산자는 자동으로 4개가 주어질 것이다.
    # 4C1 * 3C1 * 2C1 * 1C1 = 24 가지 경우의 수
    # 근데 그 중에 중복된거를 골라야 하니 / 중복의 갯수로 나눠주면 된다
    # 총 경우의 수 10! / 144 # 브루트포스 충분히 가능
    # 연산자 가지고 Combination Set 을 만들자.
    # cnt_index_list 를 가지고 조합을 할 것임
    # 총 N-1 개의 연산자를 선택해서 나열해야함
    # cnt_index_list 의 index 조합을 골라보자
    total_perm = set()  # 중복이 제거되므로, /N! 이 진행된다
    permutation([])

    max_val = -1000000000
    min_val = 1000000000

    for single_order in total_perm:
        start = nums[0]
        # print("s--------")
        for i in range(len(nums) - 1):
            if single_order[i] == str(0):  # 덧
                start += nums[i + 1]
            if single_order[i] == str(1):  # 뺄
                start -= nums[i + 1]
            if single_order[i] == str(2):  # 곱
                start *= nums[i + 1]
            if single_order[i] == str(3):  # 나
                re_ = False
                if start < 0:
                    re_ = True
                    start *= -1
                start //= nums[i + 1]
                if re_:
                    start *= -1
        # print(single_order, start)
        # print("e--------")
        max_val = max(max_val, start)
        min_val = min(min_val, start)

    print(max_val)
    print(min_val)


def main():
    # pro1()
    pro2()


main()
