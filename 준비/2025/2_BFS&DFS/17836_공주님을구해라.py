import sys
from collections import deque


# 1T
# 한번의 BFS 로 퍼져가면서, 그람을 가지고 있는지 없는지 상태를 토대로 BFS 를 돌린다
# 없는 상태로 간 Path 들을 가지 못하므로, visited 에 중복자를 is_super 와 함께 넣어서 중복X 를 체크한다
# 시간 초과

# 2T
# 어디서 줄일수 있을지 살펴보다가, 사실 무기를 얻었다면 더이상 BFS를 할 필요가 없는 것 같음 (is_super 는 사용될시에는 항상 False 이므로 고려 불필요)
## 결국 반례를 확인했지만, elapsed>T 이기 전에 dq 이 비어질 수도 있다 (벽 뚫을 수 있는 경우를 안넣는경우)
## 그렇다면 이런 경우가 언제인지 생각해보면 된다.

# 애초에 모든 경우에 수가 0 이상 <T 이하였으면 됐다.. elasped_when_super 이딴걸 왜 했지.. 바보였다

def solution(N, M, T, castle):
    di, dj = [1, 0, -1, 0], [0, -1, 0, 1]
    visited = [(0, 0)]
    dq = deque()
    dq.append(((0, 0), 0))
    when_super = -1  # 칼을 얻은 순간 계산되는 최단거리
    while dq:

        pos, elapsed = dq.popleft()
        if elapsed > T:
            # super 를 얻은 상태라면 확인해볼 가치가 있다.
            if 0 < when_super <= T:
                return when_super
            return "Fail"

        # 도달했을 경우, 무기가 있다면 바로 사용할 수 있다
        if castle[pos[0]][pos[1]] == 2:
            when_super = elapsed + (N - 1 - pos[0]) + (M - 1 - pos[1])  # 기록해둔다

        if pos == (N - 1, M - 1):  # when_super 를 얻지 못했는데, 0이라서
            # super 를 얻지 못했다면?
            if when_super > 0:
                return min(elapsed, when_super)
            else:
                return elapsed

        for k in range(4):
            mi, mj = pos[0] + di[k], pos[1] + dj[k]
            if 0 <= mi < N and 0 <= mj < M and (mi, mj) not in visited:
                if castle[mi][mj] != 1:  # 벽이 없을 경우에만 통과한다
                    visited.append((mi, mj))
                    dq.append(((mi, mj), elapsed + 1))

    # deque 이 비어져서 나왔는데, super 가 이미 기록이 되었을 경우
    if 0 < when_super <= T:
        return when_super
    return "Fail"


# 성의 크기 N,M, 제한시간 T
sys.stdin = open("input_17836.txt")
input = sys.stdin.readline

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, T, castle))
