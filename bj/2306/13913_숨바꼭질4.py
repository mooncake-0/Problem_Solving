import sys
from collections import deque

'''
포인트
 - BFS의 역추적이 주제
 - 1 시도 : path 에 계속 더해주면서, path[:] 를 통해 계속 복사해주면서 넘겨주는 풀이로 시도
    --> 솔직히 안될줄 알고 있었음. 엔간하면 복사는 하면 안됨. 
 - 2 시도 : ref 를 넘겨주면 안되는 상황이므로, str 을 통해 value 를 넘겨줌으로써 마지막에 split 해주는 방법을 시도 - 성공
 - 풀이들을 살펴보니 BFS의 역추적이 주제였음 > 또다른 배열을 통해서 "현재 보고 있는 값이 어디에서 왔는지" 를 저장해준다. > 혹은 약간 Tree 같기도 한듯
 - 잘 판단해서 풀었으나, 중요한 주제이므로 다시 풀어볼 필요가 있음
 - [BFS의 역추적] 확실히 알고 가기, 이왕이면 DFS의 역추적까지 이기회에 마스터 해버리면 좋을 듯
'''

sys.stdin = open("input_13913.txt")
input = sys.stdin.readline

start, tg = map(int, input().split())
visited = [0] * 100001
visited[start] = 1


def pro1():
    dq = deque()
    dq.append((start, 0, str(start)))

    while dq:

        cp, times, paths = dq.popleft()

        if cp == tg:
            print(times)
            return paths

        for x in range(3):
            if x == 0:
                if 0 <= cp + 1 <= 100000 and visited[cp + 1] == 0:
                    visited[cp + 1] = 1
                    dq.append((cp + 1, times + 1, paths + "." + str(cp+1)))

            elif x == 1:
                if 0 <= cp - 1 <= 100000 and visited[cp - 1] == 0:
                    visited[cp - 1] = 1
                    dq.append((cp - 1, times + 1, paths + "." + str(cp-1)))

            else:
                if 0 <= cp * 2 <= 100000 and visited[cp * 2] == 0:
                    visited[cp * 2] = 1
                    dq.append((cp * 2, times + 1, paths + "." + str(cp*2)))

def main():
    a = pro1()
    print(*a.split("."))

main()
