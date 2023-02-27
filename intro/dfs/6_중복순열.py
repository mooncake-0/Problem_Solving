import sys

sys.stdin = open("input_6.txt")

T = int(input())


def DFS(node):  # node = m 번째 뽑기
    global cnt
    if node > m:
        cnt += 1
        for a in selected:
            print(a, end=" ")
        print()
        return
    else:
        for i in range(1, n + 1):  # 이번엔 뭘 뽑고 빼는지를 제어
            selected.append(i)
            DFS(node + 1)
            selected.remove(i)


for _ in range(T):
    n, m = map(int, input().split())
    # 1 ~ n 까지 중 중복 허용해서 m개 뽑기 (1,1)
    # m 개 뽑기 기준으로 가야함 ( depth = m )
    selected = []
    cnt = 0
    DFS(1)
    # DFS 를 탈출하면 selected 는 빈 상태 -> 왜냐면 결국엔 모든 마지막엔 뽑은것을 빼기 때문
    # 그래서 cnt 라는 변수가 따로 필요
    print(cnt)
