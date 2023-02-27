import sys

sys.stdin = open("input_8.txt")


def DFS(node):
    global cnt
    if node > m:
        cnt += 1
        # print(used)
        return
    else:
        for x in range(1, n + 1):
            # used 에 없다면 x 를 사용하고, used 에 넣을 거다.
            # 3, 1 과 1, 3 은 다르므로, 이정도로 충분
            if x not in used:
                used.append(x)
                DFS(node + 1)
                used.remove(x)


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    # 순열인 것을 파악했다면, 순서상 중복되면 안되는 것임을 확인
    # 즉, 1,3 을 선택하는 것과 3,1 을 선택하는 것은 다른 것 (조합에선 같은 것)
    # 어쩄든 m 개를 선택해야 하므로, m depth 대로 움직여야 한다는 점부터 파악
    used = []
    cnt = 0
    DFS(1)
    print(cnt)
    print("===================")