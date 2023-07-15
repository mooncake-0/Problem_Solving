import sys

'''
포인트
 - 톱니바퀴를 바로 회전시키면 안됐음 (알고 있었음에도 그렇게 짬..) 
 - 상황을 저장하고 마지막에 수행하는 그런 느낌 문제 많이 풀어봤으니.. 
 - 뿐만 아니라 사소한 실수들을 하기 좋은 문제
 - 차분히 구현해내는 습관을 가지면 좋을듯
 - 뭔가 안되11001100
00001101
11000100
11010001
10
3 1
1 -1
3 1
2 -1
3 1
2 -1
4 1
1 1
3 1
2 -1도 프린팅 하면서 디버깅 차분히
'''

sys.stdin = open("input_14891.txt")
input = sys.stdin.readline

gear_pos = [list(map(str, input().strip())) for _ in range(4)]
K = int(input())

def print_gear():
    print("printing-----")
    for x in gear_pos:
        print(x)
    print("finished-----")


# 시계방향으로 회전 = 1 0 1 0 1 1 1 1  --> 1 1 0 1 0 1 1 1
def watch_dir(idx):
    tmp = ['0'] * 8
    tmp[0] = gear_pos[idx][7]
    for i in range(1, 8):
        tmp[i] = gear_pos[idx][i - 1]
    gear_pos[idx].clear()
    gear_pos[idx] = tmp


# 반시계 회전 = 1 0 1 0 1 1 1 1 --> 0 1 0 1 1 1 1 1
def op_watch_dir(idx):
    tmp = ['0'] * 8
    tmp[7] = gear_pos[idx][0]
    for i in range(0, 7):
        tmp[i] = gear_pos[idx][i + 1]
    gear_pos[idx].clear()
    gear_pos[idx] = tmp


for cnt in range(K):
    numb, real_dir = map(int, input().split())
    numb -= 1

    ''' 바로 회전시키면 안되므로 '''
    ''' 방향을 결정한 뒤 저장해 두고, 최종에 회전한다'''
    descision_maker = [0] * 4
    descision_maker[numb] = real_dir

    l_idx = numb
    spin_dir = real_dir * -1

    while l_idx > 0:
        if gear_pos[l_idx][6] != gear_pos[l_idx - 1][2]:  # 두개가 다르다면
            descision_maker[l_idx-1] = spin_dir
        else:
            break

        l_idx -= 1
        spin_dir *= -1 # 다음회전 방향은 반대여야 한다

    r_idx = numb
    spin_dir = real_dir * -1

    while r_idx < 3:
        if gear_pos[r_idx][2] != gear_pos[r_idx + 1][6]:  # 두개가 다르다면
            descision_maker[r_idx + 1] = spin_dir
        else:
            break

        r_idx += 1
        spin_dir *= -1

    # 마지막에 일괄 회전한다
    for i in range(4):
        if descision_maker[i] == 1: # 시계방향
            watch_dir(i)
        elif descision_maker[i] == -1:
            op_watch_dir(i)
        else:
            pass

score = 0
for i in range(4):
    if gear_pos[i][0] == "1":
        score += pow(2, i)

print(score)
