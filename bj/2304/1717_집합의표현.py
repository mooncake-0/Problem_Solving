import sys

'''
포인트
    - 1T 때는 NAIVE 하게 해결해봄. SET 계속 생성. 메모리 초과
    - 2T 때는 root 를 활용해봄. root set 들만두고 합쳐지는 녀석들은 다 root node 로 변환해줌 > 메모리 초과
    - 3T > 2T 가 메모리초과 난다는건 SET 이 등장하면 안된다는 거인듯
    ---- 완전한 NODE TREE 로 만들어서 해야 한다
    - 완전한 NODE TREE 만들었는데도 계속 시간 초과 남.. 
    - node tree 변경을 어떻게 해보려 했는데, 지금 구조가 맞음( 바꾸면 recursion - error 발생 ) 
    - 최적화가 필요한 시점 

    - 여기서 UNION - FIND 에 대한 이론을 좀 봤음
    - root 를 계속해서 찾는 논리는 불가피한 논리
    - 그리고 집합이 더 적은거를 합치는게 맞다 이거는 set 을 가지고 union - find 를 할 때고, TREE 는 set 을 가지고 있기 때문에 크기를 판단할 수가 없음
    - TREE 최적화는 path- compression 기법 사용
    - 지속적으로 node 를 root 로 바꿔줌으로써 경로를 엄청나게 압축시켜준다.
    - root 를 가지고 오는 속도가 훨씬 빨라짐. 
    - 아래 findRoot 함수 살짝 수정해줌으로써 바로 통과됨. 

'''

sys.stdin = open("input_1717.txt")
input = sys.stdin.readline
n, m = map(int, input().split())


def merge1(a, b):
    global judger
    tmp = set(list(judger[a]) + list(judger[b]))
    judger[a] = tmp
    judger[b] = tmp


def judge1(a, b):
    global judger
    if judger[a] == judger[b]:
        print("YES")
    else:
        print("No")


def pro1():
    global judger
    judger = dict()
    for i in range(n + 1):
        tmp = set()
        tmp.add(i)
        judger[i] = tmp


def merge2(a, b):
    global judger
    if b < a: a, b = b, a
    if a == b:
        return

    if type(judger[a]) != set:
        # 다른 쪽으로, root 로 이동해야 함
        index_a, root_set = findRootSet(a)

        if type(judger[b]) != set:  # 숫자란 뜻
            index_b, root_set_addee = findRootSet(b)
        else:
            root_set_addee = judger[b]

        # root_set_addee 에 있는 모든 애들이 root_set 으로 옮겨져야 한다
        for index in root_set_addee:
            judger[index] = index_a
            root_set.add(index)

    else:  # a 가 root 중 하나임

        if type(judger[b]) != set:  # 숫자임
            index_b, root_set_addee = findRootSet(b)
        else:
            root_set_addee = judger[b]

        for index in root_set_addee:
            judger[index] = a
            judger[a].add(index)

    # print(judger)


# 재귀를 돌리면서 최종 root 를 확인한다
def judge2(a, b):
    global judger
    if type(a) != set:
        if type(b) != set:
            if a == b:
                print("YES")
            else:
                print("NO")
        else:
            # b 가 set 임
            if a in judger[b]:
                print("YES")
            else:
                print("NO")

    else:
        if type(b) != set:
            if b in judger[a]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


def pro2():
    global judger
    judger = [0] * (n + 1)
    for i in range(n + 1):
        tmp = set()
        tmp.add(i)
        judger[i] = tmp


def pro3():
    global judger
    judger = [0] * (n + 1)
    for i in range(n + 1):
        judger[i] = i
    # print(judger)


def merge3(a, b):
    global judger
    if b < a: a, b = b, a  # 기준이 필요함
    if a == b: return

    # a < b 이며, 수가 작을 수록 root 가 된다.

    if a == judger[a]:  # 현재 a 는 root 임
        if b == judger[b]:  # b 도 root 임
            judger[b] = a

        else:  # b는 set 이기 때문에, b 의 모든 것이 a 밑으로 들어가야 함
            judger[findRoot(b)] = a

    else:  # 현재 a 는 집합임
        if b == judger[b]:  # b 는 root 임
            # 당연히 b가 a 로 들어가면 됨
            # judger[b] = a
            # a 집합의 root 에게 b 는 종속된다
            judger[b] = findRoot(a)

        else:  # a 도 집합, b 도 집합임
            # recursion 돌 때,
            # 일단 보면, a가 작고 b 가 많음을 이용하고 있지 않음
            a_root = findRoot(a)
            b_root = findRoot(b)
            judger[b_root] = a_root  # 그냥 합쳐보자

    # print(judger)


def judge3(a, b):
    # 걍 root 가 같은지 확인하면 됨
    if a == b:
        print("YES")
        return
    a_root = findRoot(a)
    b_root = findRoot(b)
    if a_root == b_root:  # 뿌리가 같다
        print("YES")
    else:
        print("NO")


# 각 숫자별로 dict 을 주고, set 을 배정 해주기?
# pro1()
# pro2()
pro3()


def findRootSet(num):  # pro2 에서 사용함
    global judger

    if type(judger[num]) != set:  # 자신이 아닐경우
        return findRootSet(judger[num])
    else:  # 같을 경우 최종 목적지 도착함
        return (num, judger[num])  # 해당 set 을 return 함


def findRoot(num):
    global judger
    if num != judger[num]:
        ### 이 한줄 추가하는 걸로 PATH-COMPRESSION 기법이 된다
        ### 모든 집합의 root 를 찐 root 로 변경해,
        ### 추후 사용될 recursion depth 를 지속해서 줄여나간다.
        judger[num] = findRoot(judger[num])
        return judger[num]
    else:
        return num


for _ in range(m):
    cmd, a, b = map(int, input().split())
    # if cmd == 0: merge2(a, b)
    # if cmd == 1: judge2(a, b)
    if cmd == 0: merge3(a, b)
    if cmd == 1: judge3(a, b)
