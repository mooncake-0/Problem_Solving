import sys

# 한줄 평 : 그냥 계속 리펙토링 하다보면 언젠간 된다. 15번과는 약간 다름.
# 15번은 최적화 관점에서 뭐가 잘못되었는지 몰랐던 수준. (BFS에 중복이 들어가던 문제)
# 기존 로직에서 반례 발견 --> 반례 사례 확인 --> 문제 원인 확인 --> 지속적으로 해결방안 생각 (이번 문제 같은 경우는 조건절의 재설정)

sys.stdin = open("input_16.txt")


def is_movable(i, j):
    if i < 0 or i >= 10 or j < 0 or j >= 10:
        return False
    if ladders[i][j] != 1:
        return False
    return True


def DFS(cur_position):  # node : 현재 내려가고 있는 위치를 말한다
    global anw, prev_position
    # print(cur_position, prev_position)
    if cur_position[0] == 9:
        if ladders[cur_position[0]][cur_position[1]] == 2:
            anw = starting_index
            return
    else:
        # 양옆이 우선권을 가진다.
        is_moved = False
        if is_movable(cur_position[0], cur_position[1] + 1) or is_movable(cur_position[0], cur_position[1] - 1):
            if prev_position[1] - 1 == cur_position[1]:  # 왼쪽으로 이동중
                if is_movable(cur_position[0], cur_position[1] - 1):
                    prev_position = [cur_position[0], cur_position[1]]
                    DFS((cur_position[0], cur_position[1] - 1))
                    is_moved = True
            elif prev_position[1] + 1 == cur_position[1]:  # 오른쪽으로 이동중
                if is_movable(cur_position[0], cur_position[1] + 1):
                    prev_position = [cur_position[0], cur_position[1]]
                    DFS((cur_position[0], cur_position[1] + 1))
                    is_moved = True

        if is_moved == False:  # 여기까지 그냥 왔으면 내려가야 함
            prev_position = [cur_position[0], cur_position[1]]
            # 양 옆이 있는지 확인, 있으면 무조건 그 쪽으로 내려가야함
            if is_movable(cur_position[0] + 1, cur_position[1] - 1):  # 왼쪽 사다리
                DFS((cur_position[0] + 1, cur_position[1] - 1))
            elif is_movable(cur_position[0] + 1, cur_position[1] + 1):  # 오른쪽 사다리 # 양쪽에 동시에 사다리가 놔지는 경우는 없음
                DFS((cur_position[0] + 1, cur_position[1] + 1))
            else:  # 둘다 그냥 통과할 경우 아래로 내려간다
                DFS((cur_position[0] + 1, cur_position[1]))


T = int(input())

for _ in range(T):

    ladders = [list(map(int, input().split())) for _ in range(10)]
    prev_position = [0, 0]
    anw = -1
    for starting_index in range(10):
        if ladders[0][starting_index] == 1:  # 시작 포지션
            # print(starting_index)
            prev_position = [0, starting_index]
            DFS((0, starting_index))
    print(anw)