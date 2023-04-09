import sys

'''
1차 시도 > NAIVE 하게 함 (using 배열이 계속 참조되어, 최종적으로 다 빈상태이다. copy 를 해서 저장시켜준다) 
2차 시도 > 메모리초과 --> combination 사용된 것들 저장시 .copy 사용 수정 (tuple 을 사용해서 참조되지 못하게 한다)
3차 시도 > 메모리초과 --> combs 배열에 저장하는 것이, 앞으로 돌아야 할 모든 원소들을 저장하기 때문에 부담일 수 있다. 
                 --> combs 를 통해 하지 않고, using 이 발견될 때마다 바로바로 판별 진행한다
4차 시도 > 시간 초과 --> ㅅㅂ..
                 --> 튜플 다시 제거. tuple 변환 과정도 O(N) 이기 때문
5차 시도 > 시간 초과 --> 왠지 모르게 답 출력된 뒤에도.. 더 돌길래 답 나오면 exit 하게 해봄
6차 시도 > 시간 초과 --> 40C20 에 대한 생각을 다시해보자
                 --> 40C20 이 TC 40 일 때 첫 DFS 조건인데 
                 
                 
                 --> 40C20 = 1000억임                 
                 --> 이분탐색으로 절대 못푸는 문제임
                 --> 

                 ---------------> 좀 아쉽다. 좀만 더 생각했으면 당연히 안된다는걸 알았을텐데. 아쉬운 문제. 
'''

sys.stdin = open("input_1047.txt")
input = sys.stdin.readline


def combination_available(tmp):  # tmp 배열이 전달된다
    global checker
    cur_length = 0

    # 최소 x, 최대 x, 최소 y, 최대 y 를 구해야 한다
    max_x = -1
    min_x = 1000000
    max_y = -1
    min_y = 1000000

    for i in range(len(trees)):
        if i in tmp:
            cur_length += trees[i][2]
        else:
            max_x = max(trees[i][0], max_x)
            min_x = min(trees[i][0], min_x)
            max_y = max(trees[i][1], max_y)
            min_y = min(trees[i][1], min_y)
    if 2 * (max_x - min_x) + 2 * (max_y - min_y) <= cur_length:
        checker = True
    # 다 돌아도 여기까지 온거면 안되는것


# 2<= N <= 40
# 나무를 잘라 울타리를 만들 거임
# 나무 심어져 있는 위치, 베었을 때 만들어지는 울타리 길이
# (x,y) l
# 0 < x,y,l < 1,000,000
# 이중배열 금지란 뜻
def combination(n, start, using):
    global combs
    if len(using) == n:
        # 저장하지 말고 바로 using 을 돌려보자.
        combination_available(using)
        if checker:
            return
    else:
        for i in range(start, len(trees)):
            using.append(i)
            combination(n, i + 1, using)
            using.pop()


def judge(mid):
    global using, combs, checker
    # mid 개를 잘라서 현재 울타리를 만들 수 있는가?
    # 결국 조합을 사용해서  자를 녀석들을 선정해줘야 한다
    # trees 중에 mid 개를 고를 예정임
    combs = []
    checker = False
    combination(mid, 0, [])
    return checker

    '''
    # 그녀석들이 없는 필드에서, 결과적인 길이로 직사각형을 만들어서 두를 수 있는지?
    for each in combs:
        cur_trees = []
        cur_length = 0

        # 최소 x, 최대 x, 최소 y, 최대 y 를 구해야 한다
        max_x = -1
        min_x = 1000000
        max_y = -1
        min_y = 1000000

        for i in range(len(trees)):
            if i in each:
                cur_length += trees[i][2]
            else:
                cur_trees.append(trees[i])
                max_x = max(trees[i][0], max_x)
                min_x = min(trees[i][0], min_x)
                max_y = max(trees[i][1], max_y)
                min_y = min(trees[i][1], min_y)
        if 2 * (max_x - min_x) + 2 * (max_y - min_y) <= cur_length:
            return True
    # 다 돌아도 여기까지 온거면 안되는것
    return False
    '''


N = int(input())

trees = []
# 4 * 3 * 40 = 480 0.48
for _ in range(N):
    *tree_pos, t_l = map(int, input().split())
    trees.append((tree_pos[0], tree_pos[1], t_l))


# mid = (lt + rt) // 2
# result = judge(mid)
# print(mid, result)
lt = 1  # 최소 한개는 잘라야 함
rt = N - 1  # 모두 자를리는 없지만 그렇게 자를 수는 있음

anw = -1
anwed = False
# mid 개를 자를 때, 될 수 있는 경우가 있는가?
# 부족하면 더 늘려줄 것
# 충분하면 더 줄여볼 것
while lt <= rt:

    if lt == rt:  # 둘이 같은 경우라면 올 때까지 온 것
        anwed = True
        result = judge(lt)
        if result:
            print(lt)
        else:
            print(lt + 1)
        exit()

    mid = (lt + rt) // 2  # mid = 3
    result = judge(mid)
    if result:  # 충분한 것, 더 적게 잘라볼 것임 # 3으로 됨!
        rt = mid - 1  # rt = 2
    else:  # 부족한 것, 더 많이 잘라볼 것임. # 1은 쭉 안되는 듯
        lt = mid + 1  # lt = 2
    anw = lt  # 이 문제 같은 경우, 안될 시에 줄여야 하기 때문에, lt 로 맞춰준다

if not anwed:
    print(anw)
    exit()
