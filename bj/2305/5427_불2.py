import sys
from collections import deque

sys.stdin = open("input_5427.txt")
input = sys.stdin.readline

'''
포인트
    - 4197 과 아예 똑같은 문제 
    - 지금 난 불과 사람 움직임 순서에서 혼돈을 겪음 (처음 움직임 처리가 문제였음)
    - 첨에 불이 움직이고, 내가 움직일 수 있는 곳들을 QUEUE 에 넣었음
    - 근데 이 때 전체 횟수 (cur_time) 을 증가시켜버려서, 두번째 경우에 불이 번지지 않은채로 내가 움직일 수 있는 곳들을 넣어버림
    - 이 때부터 쫓기는 관계가 반대가 되었다. (times == 0 일 때와 구분해주는 순간부터 정상동작하게 됨) 
    - 항상 불이 한발 늦게됨. >> 이걸 반례들 (게시판 보면서 파악해버림.. ) 
    - 이건 게시판 안봐도 TC 반례들 매핑 더 섬세히 확인했으면 됐을 부분.
    - 하지만 4197 덕분에 중복처리, 불 여러개 등은 바로 해결해 놓을 수 있었음
    - 제발... 차분하게 확인하자.. 안되는것들.. 주어진 TC 들로 해결할 수 있거나 간단한 TC 준비는 할 수 있어야 한다 

'''

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def print_maze(s_pos,ct, t):
    for x in maze:
        print(x)
    print("s_pos: ", s_pos)
    print("ct: ", ct)
    print("t: ", t)
    print("==================")


def pro1(cur_pos, fire_dq):
    global maze

    dq = deque() # 상근이 BFS
    dq.append((cur_pos, 0))
    visited = set()
    visited.add(cur_pos)
    cur_times = 0 #  움직임


    while dq:

        s_pos, times = dq.popleft()


        # print(dq)
        # print_maze(s_pos, cur_times, times)


        if times == 0 or cur_times +1 ==  times:
            if cur_times +1 == times:
                cur_times += 1
            # 불이 움직이고 # 상근이 위치여도 일단 불로 만든다
            # 상근이가 움직인 정도가 증가할 경우에만 불을 움직인다 # 같은 cur_times 동안에는 움직이지 않는다
            for _ in range(len(fire_dq)): # 현재 들어있는 불의 갯수만큼 불을 확장시키고, 다시 넣어준다
                fire_pos = fire_dq.popleft()
                for i in range(4):
                    mfi = fire_pos[0] + di[i]
                    mfj = fire_pos[1] + dj[i]
                    if 0<= mfi < I and 0<= mfj < J and maze[mfi][mfj] != '#' and maze[mfi][mfj] != '*':
                        maze[mfi][mfj] = "*"
                        fire_dq.append((mfi,mfj))

        # 상근아 달려
        for k in range(4):
            msi = s_pos[0] + di[k]
            msj = s_pos[1] + dj[k]

            if 0 <= msi < I and 0 <= msj < J and maze[msi][msj] == '.' and (msi,msj) not in visited:
                # 상근이가 움직일 수 있다
                visited.add((msi,msj))
                dq.append(((msi,msj), times+1))


            elif msi < 0 or msi >= I or msj < 0 or msj >= J: # 상근이의 탈출
                return times+1

    return "IMPOSSIBLE"




# 불은 여러개일 수 있다
def main():
    global I,J, maze

    TC = int(input())

    for _ in range(TC):
        J, I = map(int, input().split())
        fire_dq = deque()
        maze =[]
        for i in range(I):
            tmp = list(map(str, input().strip()))
            for j in range(J):
                if tmp[j] == "@": # 상근이
                    cur_pos = (i,j)
                if tmp[j] == "*": # 불
                    fire_dq.append((i,j))
            maze.append(tmp)

        print(pro1(cur_pos, fire_dq))

main()
