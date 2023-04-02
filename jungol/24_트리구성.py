import sys

'''
dict 으로 했다가 실패함
> 그냥 아예 막힘. 됐어야 하는데 안된 부분이 있는 것 같음
> 조건식이 너무 많이 들어가는 부분에서 아마 문제가 발생하지 않았을까? *****본인도 이해하지 못한 recursion 을 짠 결과******

> key 값이 int 일 수 있고 지금 경우처럼 나열되고 중복되지 않는 index 들일 경우에는.. 걍 list 로도 충분히 map 역할을 할 수 있음
> 병렬 처리가 쉬우니, list 로 가보자

'''

sys.stdin = open("input_24.txt")
input = sys.stdin.readline


# x 를 y부모 밑에 추가한다
# 사용에 추가되는 대상은 항상 x이다
def add(x, y):
    global C, P, on_use
    C[y].append(x)
    P[x] = y
    on_use[x] = 1
    print("add: C: ", C)
    print("add: P: ", P)


def root_distance(x, cnt):
    if x == 0:
        return cnt
    else:
        return root_distance(P[x], cnt + 1)

# 0 > 1 > 3 > 5
#       > 4
#   > 2

# x 로 부터 root 의 거리 a
# x 로 부터 가장 먼 자손의 거리 b 차례 출력
def query(x):
    a= root_distance(x, 0)
    print(a)


# x 를 y 의 자식노드로 변경 #통째로 그대로 들고가게되는 것
# x == y // 둘중 존재하지 않거나 // y 가 x 의 자손이면 무시
def move(x, y):
    global C, P, on_use
    if x == 0 or x == y:
        return
    if on_use[x] == 0 or on_use[y] == 0:
        return

    ''' 추가 조건 필요: y 가 x의 자손인지 판별 필요'''

    # 내 자손들에 대해서는 변경될 필요가 없음
    # 기존 나의 부모에서 나를 뺀다
    C[P[x]].remove(x)

    # y 의 자식 리스트에 나를 추가한다
    C[y].append(x)

    # 나의 부모를 바꾼다
    P[x] = y


# x 노드를 지운다. 자식이 있다면 x의 부모의 자식들이된다
# x 가 부모거나 없을시 무시한다
def remove(x):
    global C, P, on_use
    if x == 0 or P[x] == -1 or on_use[x] == 0:
        return

    # 부모의 자식 리스트에 있는 본인을 제거한다
    C[P[x]].remove(x)

    # 자식들을 확인후, 있다면 x 의 부모애 연결해준다
    for child in C[x]:
        P[child] = P[x]
        C[P[x]].append(child)

    # 자신의 모든 상태를 원복시킨다
    C[x].clear()
    P[x] = -1
    on_use[x] = 0  # 더 이상 트리에 있지 않다

    print("remove: C: ", C)
    print("remove: P: ", P)


def main():
    # q 총 10000 개 이하
    global C, P, on_use

    # 크기만큼 미리 만들어 놓자.
    # index == node 이다
    # 0 번 node 부터, 10000 번 node 까지
    C = [[] for _ in range(10001)]  # child 들이 들어오게 된다
    P = [-2] + [-1] * 9999  # root 노드는 부모가 없다
    on_use = [0] * 10001  # 지금 tree 에 있는 node 인지를 표시
    on_use[0] = 1  # root 는 항상 있다

    for q in range(int(input())):
        cmd, *val = map(str, input().strip().split(" "))
        if cmd == 'add': add(int(val[0]), int(val[1]))
        if cmd == 'query': query(int(val[0]))
        if cmd == 'move': move(int(val[0]), int(val[1]))
        if cmd == 'remove': remove(int(val[0]))


main()
