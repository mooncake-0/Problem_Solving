import sys

'''
포인트 
- dice 의 움직임을 면에 "1,2,3,4,5,6" 이라는 네이밍을 줘서 계속 제어하려고 시도함
- dir 방향도 있지만, 현재 주사위의 dir 상태까지 변수이기 때문에, 이를 제어하는건 너무 어려움. 
- "이렇게까지?? 해야 하나 싶을 때는.. 내가보기엔 일반적으로 그거보다 더 쉬운 방법이 있다"

- (이 부분 구현에 대해서는 살짝 솔루션 봄.... ㅅㅂ) 
- 면에 네이밍을 주지말고, 동서남북으로 움직였을 때 기준으로 생각해보자
- 면에 굳이 기준을 잡을 필요 없이, 현재 주사위 상태에서 1,2,3,4,5,6 일 시 동으로 움직였을 때 어떻게 움직이는지를 잡으면 된다
- 그럼 상태에 또 현재면 기준으로 1,2,3,4,5,6 이 움직일 것. 

- 1 의 정방향 위에 2가 있어서 1이 북으로 가면 2다 라는것은 틀림 ( 1이 정방향이 아닐때도 북으로 갔을 때 2라고 하기 때문 ) 
- "1 이 밑면인 상태에서 동쪽으로 움직이면 그 상태에서 왼쪽에 있던 면은 x로 움직인다" 이런식으로 들어가는 거임.. 꽤나 어려운 것 같은데
'''
sys.stdin = open("input_14499.txt")
input = sys.stdin.readline

I, J, ix, iy, k = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(I)]
TC = list(map(int, input().split()))
cur_position = (ix, iy)
cur_side = 1

move_pos = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dices = [0] * 7

# idx 1,2,3,4,5,6 면에 대한 기준--> 아래1, 위,6 정면으로16사이는2, 2왼쪽으로 순서대로 3,4,5 이렇게 지정해놓는다.
# 면에 대한 기준이 아니라, 이 고정된 자리에 대한 기준을 정해놓는 것이다
# 동쪽으로 움직일 시
def mover(dir):
    tmp_1, tmp_2, tmp_3, tmp_4, tmp_5, tmp_6 = dices[1], dices[2], dices[3], dices[4], dices[5], dices[6]
    if dir == 1:  # 동
        # 1의자리엔 기존 3이 오고, 2에 자리는 유지되고, 3의자리엔 6이오고 이런식
        dices[1], dices[2], dices[3], dices[4], dices[5], dices[6] = tmp_3, tmp_2, tmp_6, tmp_4, tmp_1, tmp_5
    elif dir == 2:  # 서
        dices[1], dices[2], dices[3], dices[4], dices[5], dices[6] = tmp_5, tmp_2, tmp_1, tmp_4, tmp_6, tmp_3
    elif dir == 3:  # 북
        dices[1], dices[2], dices[3], dices[4], dices[5], dices[6] = tmp_4, tmp_1, tmp_3, tmp_6, tmp_5, tmp_2
    else:  # 남
        dices[1], dices[2], dices[3], dices[4], dices[5], dices[6] =  tmp_2, tmp_6, tmp_3, tmp_1, tmp_5, tmp_4

def pro1(dir):
    global cur_position, maze

    mi = cur_position[0] + move_pos[dir][0]
    mj = cur_position[1] + move_pos[dir][1]

    if mi < 0 or mi >=I or mj < 0 or mj >= J:
        return -1


    cur_position = (mi,mj) # 현재 위치 최신화

    mover(dir) # 움직임 수행
    # mover 기준으로 움직인후 dices[1] 이 고정적인 밑면이다

    if maze[mi][mj] == 0: # dice의 수를 밑면에 새긴다
        maze[mi][mj] = dices[1]
    else: # maze 의 수를 dice의 밑면에 새기고, maze 의 수를 지운다
        dices[1] = maze[mi][mj]
        maze[mi][mj] = 0

    # 반대편의 숫자를 반환한다 # 6번 포지션에 있는 숫자임.
    return dices[6]




def main():
    for dir in TC:
        a = pro1(dir)
        if a == -1:
            continue
        print(a)



''' 잘못된 시도 1트
    # idx 1,2,3,4 --> 동, 서,북, 남 이동시 바닥에 닿는 면
    # idx 0 --> 해당 주사위의 반대면이 적혀 있다.
    dice_movement = [[] for _ in range(7)]

    # 1이 정방향 기준이라는게 확실히 잡혀야 함 --> 이걸 같이 구현해주는게 너무 어려움. 어렵다기보단 헷갈리고 복잡
    dice_movement[1] = [6, 3, 4, 2, 5]
    dice_movement[2] = [5, 0, 0, 6, 1]
    dice_movement[3] = [4, 6, 0, 0, 0]
    dice_movement[4] = [3, 1, 0, 0, 0]
    dice_movement[5] = [2, 0, 0, 1, 6]
    dice_movement[6] = [1, 4, 0, 5, 2]
'''

main()
