import sys

sys.stdin = open("input_2.txt")
input = sys.stdin.readline


def judge(route, cur, dest):
    if cur == dest:
        return True
    if cur in route:
        if cur + 1 in route[cur]:
            return judge(route, cur + 1, dest)
        else:
            return False
    else:
        return False


def solution(N, A, B):
    # N ~ 100,0000
    route = dict()
    for idx in range(len(A)):
        if A[idx] not in route:
            tmp = set()
            tmp.add(B[idx])
            route[A[idx]] = tmp
        else:
            route[A[idx]].add(B[idx])

        ''' 반대편 '''
        if B[idx] not in route:
            tmp = set()
            tmp.add(A[idx])
            route[B[idx]] = tmp
        else:
            route[B[idx]].add(A[idx])

    return judge(route, 1, N)


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = solution(N, A, B)
if a:
    print("yes")
else:
    print("no")
