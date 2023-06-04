import sys
from collections import deque

sys.stdin = open("input_1600.txt")
input = sys.stdin.readline

'''
포인트

- 정말 바보같이 푼 문제
- 진작에 h_count 가 적용되는 원리를 생각했으면 금방 풀었을 듯
- h_count 가 그냥 고려되면 되는데, horse 로 움직일 때만 h_count 가 증가된 애들이 추가될 것이라 생각했던 것이 문제
- (~~,1), (~~,1), (~~,2) 일 경우
- 1번에서 돈 곳 == (~~,2 로 들어가게 됨)
- 2번에서 돌 곳이 중복되는 것을 방지해줌
- 이렇게 정해진 것 이외에는 너가 건드릴 필요가 없음. 
- 너가 쓰는 BFS가 어떻게 도는지 정확하게 알고 돌려야 한다 
- BFS탐색의 기본기에 충실하지 못해서 아쉬웠던 문제 
'''

K = int(input())
J, I = map(int, input().split())  # 1~200
maze = [list(map(int, input().split())) for _ in range(I)]

n_di, n_dj = [0, 1, 0, -1], [1, 0, -1, 0]
h_di, h_dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
cp = (0, 0)


# K 번 이후에는 일반적으로밖에 못 움직인다
# 0은 평지이고, 1은 장애물이다
# 말만이 장애물을 뛰어넘을 수 있다.

def pro1():
    dq = deque()
    dq.append((cp, 0, 0))

    huc_visited = set()
    huc_visited.add((cp, 0))

    while dq:

        cur_pos, times, h_used = dq.popleft()  # h_used 횟수가 K를 채우게되면 더이상 사용하지 못함
        if cur_pos == (I - 1, J - 1):
            return times

        # 내가 말에 대해서 사용하거나, normal 을 사용하거나 모든 경우가 BFS에서 고려되어야 한다
        for i in range(4):
            mi = cur_pos[0] + n_di[i]
            mj = cur_pos[1] + n_dj[i]

            # 일반적으로 움직이는 경우는 일반적인 case 들에 속한다
            if 0 <= mi < I and 0 <= mj < J and maze[mi][mj] == 0 and ((mi, mj), h_used) not in huc_visited:
                huc_visited.add(((mi,mj), h_used))
                # 가려는 곳에 사용된 h_used 가 있다면?
                dq.append(((mi, mj), times + 1, h_used))

        # 말에 대해서 사용할 수 있는 경우도 모두 BFS에서 고려되어야 한다
        # 갈 수 있는 곳이 중복되지 않으므로, visited 에 대한 점은 고려하지 않는다
        if h_used < K:
            for i in range(8):
                hi = cur_pos[0] + h_di[i]
                hj = cur_pos[1] + h_dj[i]
                if 0 <= hi < I and 0 <= hj < J and maze[hi][hj] == 0 and ((hi,hj), h_used+1) not in huc_visited:
                    huc_visited.add(((hi,hj), h_used+1))
                    dq.append(((hi, hj), times + 1, h_used + 1))

    return -1


def main():
    print(pro1())


main()
