import sys

'''
한시간 반정도 걸림 
포인트 
    - 구현해야할 순서를 확실히 정리
    - 뭔가 헷갈리는 듯한 로직을 해야하는데 살짝의 노가다가 곁들여질 수 있다면 빠른 판단을 하는 것도 ㄱㅊ
    - 사실 미세한 로직 구현, TC 분석하면서 에러 분석 이게 다였던 문제
    - 할만했지만, 너무 오래걸렸음 (빡구현... 이라 보기엔 살짝 애매.. 하지만 극한의 구현 문제 

'''
sys.stdin = open("input_20057.txt")
input = sys.stdin.readline
N = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]

for idx in range(N):
    tmp = [0] + list(map(int, input().split()))
    board[idx + 1] = tmp

# 현태풍정보
tp = (N // 2 + 1, N // 2 + 1)
DIR = 3  # -1 씩 하면서 전진
DIR_MAP = {1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)}

COUNT_MOVE = 1  # NEEDS_ 가 0 이 되면 1씩 올라간다
EACH_MOVE_COUNT = 0
NEEDS_ = 2  # 각 MOVE 는 두번씩 수행된다

ANW = 0


# DIRECTION = 동 : 1, 남 : 2, 서 : 3, 북 : 4
# 토네이도의 이동 로직
# 토네이도는 st 에서 시작하여 1, 1, 2,2, 3,3, 4,4, 로 돌면서 이동한다
def moveTorn(ci, cj):
    global DIR, COUNT_MOVE, NEEDS_, EACH_MOVE_COUNT
    move = DIR_MAP[DIR]
    mi = ci + move[0]
    mj = cj + move[1]
    if mi < 1 or mi > N or mj < 1 or mj > N:  # 종료
        return (-1, -1)  # 종료 조건

    # 움직였으므로, 필요한 것들을 수행
    # EMC 가 CM 과 같으면 그 때 방향을 바꾼다
    EACH_MOVE_COUNT += 1  # 이미 움직인다
    # NEEDS_ -= 1  # 이미 한번 움직였음

    if EACH_MOVE_COUNT == COUNT_MOVE:  # 방향을 바꿔야 한다
        DIR -= 1

        if DIR == 0: DIR = 4
        EACH_MOVE_COUNT = 0  # 이번거 다 움직였으면 0 으로 바꾼다

        NEEDS_ -= 1
        if NEEDS_ == 0:  # 그 와중에 NEEDS 가 끝났으면 움직여야 하는 횟수 1 증가
            NEEDS_ = 2
            COUNT_MOVE += 1

    return (mi, mj)


# DIR = 3 을 기준으로 포지션 별 모래 비율을 표시해보자
SAND_MOVE_MAP = {
    3: {
        (1, 0): 7, (-1, 0): 7, (2, 0): 2, (-2, 0): 2,
        (-1, 1): 1, (1, 1): 1, (1, -1): 10, (-1, -1): 10,
        (0, -2): 5, (0, -1): 0
    },
    4: {
        (0, 1): 7, (0, -1): 7, (0, 2): 2, (0, -2): 2,
        (1, 1): 1, (1, -1): 1, (-1, 1): 10, (-1, -1): 10,
        (-2, 0): 5, (-1, 0): 0
    },
    1: {
        (-1, 0): 7, (1, 0): 7, (-2, 0): 2, (2, 0): 2,
        (1, -1): 1, (-1, -1): 1, (-1, 1): 10, (1, 1): 10,
        (0, 2): 5, (0, 1): 0
    },
    2: {
        (0, -1): 7, (0, 1): 7, (0, -2): 2, (0, 2): 2,
        (-1, -1): 1, (-1, 1): 1, (1, -1): 10, (1, 1): 10,
        (2, 0): 5, (1, 0): 0
    }
}


def moveSands(ci, cj):  # 이번 이동에 대한 움직임 파악이 필요 (도착 지점의 sand)
    global ANW
    # DIR = 3 이면 SAND_MOVE_MAP 그대로
    # 현재 토네이도가 여기로 DIR 을 가지고 이동을 한 상태임
    # 그 DIR 에 대한 모래 흩날림 비율을 계산해준다
    # 내가 여기로 온 방향이 중요
    # EACH_MOVEMENT = 0 일 때마다 방향이 바뀌므로,
    # EACH_MOVEMENT = 0 이면 DIR -1 을 해주고 넣는다
    if EACH_MOVE_COUNT == 0:

        tmp = DIR + 1  # 이전 방향
        if tmp == 5:  # 4가 넘어가면
            tmp = 1  #
        movement = SAND_MOVE_MAP[tmp]
    else:
        movement = SAND_MOVE_MAP[DIR]

    pre_amount = board[ci][cj] # 현 지점 모래의 양 (board 값 끝까지 고정)

    for pos in movement: # 모래가 가야하는 지점들

        spi = ci + pos[0]
        spj = cj + pos[1]

        if movement[pos] == 0: # 남은 모래가 이동
            leftover_pos = (spi, spj)
            continue

        out_amount = int(board[ci][cj] * (movement[pos] / 100))  # 고정된 값에서 비율만큼 계산
        # 계산시 소숫점 버리므로 여기서 0.5 이런건 0 인 것
        pre_amount -= out_amount # 첫 모래 양에서 날라가는 만큼 계속 뺀다

        # 가는 지점이 line 밖이라면
        if spi < 1 or spi > N or spj < 1 or spj > N:
            ANW += out_amount
        else: # 안이면 현재 그 곳에 있는 모래에 이동되는 모래의 양을 적재한다
            board[spi][spj] += out_amount

    # 다 돌면 pre_amount 는 처음 모래에서 남은 양, board[ci][cj] 는 그대로
    # 남은 양이 밖이여야 한다면
    if leftover_pos[0] < 1 or leftover_pos[0] > N or leftover_pos[1] < 1 or leftover_pos[1] > N:
        # 날라가는 양에 더한다
        ANW += pre_amount
    # 그 곳에 남은 양을 전부 옮긴다
    else:
        board[leftover_pos[0]][leftover_pos[1]] += pre_amount  # 남은 양
    # 움직인 곳은 0 이된다
    board[ci][cj] = 0


while True:
    tp = moveTorn(tp[0], tp[1])
    if tp == (-1, -1):
        break
    moveSands(*tp)
    # for x in board:
    #     print(x)
    # print("-==-=-=-=-=-=-=-=-=-==-=-=-")
print(ANW)
# tp 가 내 다음 포지션이다.
# tp 에 대하여 각 모래 흩날리는 로직을 실행하면 된다
