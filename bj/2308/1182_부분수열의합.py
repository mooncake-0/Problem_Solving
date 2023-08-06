import sys

sys.stdin = open("input_1182.txt")
input = sys.stdin.readline

N, S  = map(int, input().split())
numbs = list(map(int, input().split()))

def dfs(depth, cur_sum):
    global used_, cnt
    if depth == len(numbs):
        if cur_sum == S and len(used_) != 0:
            cnt += 1
    else:
        # 사용 했을 때와, 안했을 때를 분리해서 가정한다
        used_.append(numbs[depth])
        dfs(depth + 1, cur_sum + numbs[depth])
        used_.pop()
        dfs(depth + 1, cur_sum)

cnt = 0
used_ = []
dfs(0, 0)
print(cnt)

