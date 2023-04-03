import sys
from collections import deque

'''
그닥 없음. 쉬운 문제. 
이젠 기본적으로 일일이 탐색보단 인덱싱을 통해 시간 감소시키는건 기본..

시험 전에 알고 가야할 시간 복잡도 정리해야할듯! 
'''
sys.stdin = open("input_1697.txt")
input = sys.stdin.readline

# 점프냐, -1, 이냐, +1 이냐를 기준으로 BFS 탐색을 진행한다

visited = [0] * 100001


def main():
    position, target = map(int, input().split())
    dq = deque()
    dq.append((position, 0))
    visited[position] = 1

    while dq:

        cur_position, cnt = dq.popleft()

        if cur_position == target:  # 제일 빨리 도달이 제일 빠른 시간
            print(cnt)
            break

        for i in range(3):
            if i == 0:  # cur_position +1
                if cur_position + 1 <= 100000 and visited[cur_position + 1] != 1:
                    dq.append((cur_position + 1, cnt + 1))
                    visited[cur_position + 1] = 1
            if i == 1:  # cur_position -1
                if cur_position - 1 >= 0 and visited[cur_position - 1] != 1:
                    dq.append((cur_position - 1, cnt + 1))
                    visited[cur_position - 1] = 1

            if i == 2:  # cur_position *2
                if cur_position * 2 <= 100000 and visited[cur_position * 2] != 1:
                    dq.append((cur_position * 2, cnt + 1))
                    visited[cur_position * 2] = 1


main()
