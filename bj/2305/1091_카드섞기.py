import sys

sys.stdin = open("input_1091.txt")
input = sys.stdin.readline

N = int(input())  # N = 3t (t = 1~16)
DEST = list(map(int, input().split()))
S = list(map(int, input().split()))


def judge(deck):  # 현재 덱을 분출시 DEST대로 나뉘어 지는지 확인한다
    getting = [0] * N
    for i in range(N):
        if i % 3 == 0:  # 0, 3 째 카드는 0번이 가지게 된다
            person_num = 0
        elif i % 3 == 1:  # 1번이 가지게 된다
            person_num = 1
        else:
            person_num = 2
        getting[deck[i]] = person_num
    if getting == DEST:
        return True
    else:
        return False


def rotate(deck):
    # deck 을 S 의 방법대로 섞는다
    # i 번째의 카드는 S[i] 번째로 이동한다
    # 기존: a b c d e f
    # 섞기: 1 4 0 3 2 5 # 이건 포지션을 말한다
    # 섞후: c a e d b f
    result = [0] * N
    for i in range(N):
        result[S[i]] = deck[i]
    return result


ref = [0] * N
for i in range(N):
    ref[i] = i

start = [0] * N
for i in range(N):
    start[i] = i

times = 0
not_possible = False
# while 문 돌리면서 현재 배열 = DEST 로 가는지 확인

while not judge(start):
    times += 1
    start = rotate(start)
    # 돌렸는데, 결국 처음과 같아짐
    if start == ref:
        not_possible = True
        break

if not_possible:
    print(-1)
else:
    print(times)

# 0,1,2,3,4,5
# 1회 섞으면 S[i] 로 변경
# 1 4 0 3 2 5 (0 > 2 / 1> 0 / 2 > 4 / 3 > 3 / 4 > 1 / 5 > 5)
# 4 2 1 3 0 5 (이게 두번째 섞었을 때임)
# 0 1 2 0 1 2 > P (0,1,2) # 0번째 위치에 있는 카드는 최종적으로 0에게
# 1 4 0 3 2 5 > S # 섞는 방법 > 카드를 섞으면 i 번째 카드는 S[i] 에게 이동한다

# 모든 숫자가 P[i] 대로 맞춰졌을 때 종료한다
