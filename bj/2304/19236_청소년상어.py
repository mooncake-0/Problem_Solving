import sys
import copy

sys.stdin = open("input_19236.txt")
input = sys.stdin.readline

'''
포인트
 - 필드가 작으므로 시간과 공간적으로 여유가 있음
 - 내부 로직 구현이 더 중요한 문제
 - deepcopy 와 shallow copy 의 차이를 이해 
 - 셸로 커피는 1차적인 배열에서만 복사를 지원해준다 
 - dict 을 안쓴 풀이도 있더라 .. 
 - 원인 분석을 열심히 해봤던 문제 ..
'''


# 해당 번호일 경우 이동해야 하는 방향을 알려준다
dir = [0, [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]


def print_fishmap(cur_map, cur_dict):
    print(id(cur_map))
    print(cur_dict)
    print("-----------------------------")
    for x in cur_map:
        print(x)
    print("-----------------------------")


def is_fish_movable(cur_map, position):
    if position[0] < 0 or position[0] >= 4:
        return False
    if position[1] < 0 or position[1] >= 4:
        return False
    if cur_map[position[0]][position[1]][0] == -1:
        return False
    return True


def moveFish(cur_map, cur_dict, eaten):
    for cur_fish in range(1, 17):
        if cur_fish not in eaten:  # eaten 에 있으면 dict 에 없음

            c_fish_pos = cur_dict[cur_fish]
            c_fish_dir = cur_map[c_fish_pos[0]][c_fish_pos[1]][1]

            # 움직이게 한다
            moving_position = [c_fish_pos[0] + dir[c_fish_dir][0], c_fish_pos[1] + dir[c_fish_dir][1]]

            while not is_fish_movable(cur_map, moving_position):
                # 움직일 수 있는 곳이 될 때까지 c_fish_dir 를 움직인다
                c_fish_dir += 1
                if c_fish_dir == 9:
                    c_fish_dir -= 8
                moving_position = [c_fish_pos[0] + dir[c_fish_dir][0], c_fish_pos[1] + dir[c_fish_dir][1]]

            # 갈 수 있는 곳이 되었다.
            # 두 물고기를 바꾼다
            # 지도에서 위치 바꾼다
            tmp = cur_map[moving_position[0]][moving_position[1]]  # 바꾸려는 곳의 물고기, 방향
            cur_map[moving_position[0]][moving_position[1]] = [cur_fish, c_fish_dir]  # 이 장소에는 현재 물고기가 온다
            cur_map[c_fish_pos[0]][c_fish_pos[1]] = tmp

            # 물고기 position 을 업데이트 해준다
            if tmp[0] != 0:
                cur_dict[tmp[0]] = c_fish_pos
            cur_dict[cur_fish] = moving_position


# 설계가 되는 방향
# 물고기는 이제 한바퀴 쉽게 돌릴 수 있음
# 상어가 선택할 수 있는 선택지를 기준으로 DFS 를 돌릴거임
# 이 때, 지금 배열은 4*4*4 = 64
# 물고기를 다 먹어야 해도 16, > 1024 > 1MB 임
# 그리고 한 줄 당 생성될 수 있는게 3개라고 쳐도, 3MB
# 계속 생성해도 큰 문제가 안될 것 같음.

def dfs(cur_map, cur_dict, eaten):
    # 현재 지도를 중심으로, 현재 dict 을 중심으로 돌린다
    moveFish(cur_map, cur_dict, eaten)

    # 현재 상어의 위치를 파악한다
    shark_pos = cur_dict[-1]
    shark_dir = cur_map[shark_pos[0]][shark_pos[1]][1]
    avails = []
    i = 1

    # 현재 상어의 위치를 중심으로 갈 수 있는 곳들을 파악해본다
    while True:
        adder = [dir[shark_dir][0] * i, dir[shark_dir][1] * i]
        move_to = [shark_pos[0] + adder[0], shark_pos[1] + adder[1]]
        if move_to[0] < 0 or move_to[0] >= 4 or move_to[1] < 0 or move_to[1] >= 4:
            break

        # 해당 칸의 fish 가 없으면 안된다
        if cur_map[move_to[0]][move_to[1]][0] != 0:
            avails.append(move_to)
        i += 1

    # 갈 수 있는 곳이 없다면, 이번 것은 종료한다
    if not avails:
        eaten_fishes_sum.append(sum(eaten))

    else:
        for target_position in avails:
            target_idx = cur_map[target_position[0]][target_position[1]][0]  # 현재 물고기들 이동한 map 에서 우리의 tg 의 위치

            # 기존 상어의 자리는 0 으로 만든다
            cur_map[shark_pos[0]][shark_pos[1]][0] = 0
            cur_dict[-1] = [target_position[0], target_position[1]]  # 상어의 위치가 타겟으로 변경
            cur_map[target_position[0]][target_position[1]][0] = -1  # 상어가 도달 # 이거는 원복되어야 한다
            del cur_dict[target_idx]  # 먹힌 녀석은 dict 에서 제거된다
            eaten.append(target_idx)

            dfs(copy.deepcopy(cur_map), copy.deepcopy(cur_dict), eaten)

            eaten.pop()
            cur_map[target_position[0]][target_position[1]][0] = target_idx  # 상어가 다시 뱉고, 어디로 갈지 결정 상태로 돌아간다
            cur_dict[target_idx] = [target_position[0], target_position[1]]  # 먹힌 녀석의 자리가 다시 추가된다 # 이 상태로 다음 걸로 간다


# 현재 지도를 만든다
fish_map = []
# 각 fish index 별 위치를 저장해둔다
fishes_dict = dict()

for i in range(4):
    tmp = list(map(int, input().split()))
    adder = []
    for j in range(4):
        adder.append([tmp[2 * j], tmp[2 * j + 1]])
        fishes_dict[tmp[2 * j]] = [i, j]
    fish_map.append(adder)

eaten_fishes_sum = []
# 초기조건 잡기
ate = []
ate.append(fish_map[0][0][0])
del fishes_dict[ate[0]]
fishes_dict[-1] = [0, 0]
fish_map[0][0][0] = -1



dfs(copy.deepcopy(fish_map), copy.deepcopy(fishes_dict), ate)
# dfs(fish_map.copy(), fishes_dict.copy(), ate)
print(max(eaten_fishes_sum))


'''
# 상어가 자리를 잡고
# 물고기 돌리고
# 상어가 갈 수 있는 지점들을 통해 DFS 를 진행한다 (차피 다 봐야하기 때문)
# 상어는 -1 로 표기한다
def dfs(eaten):
    print("init", eaten)
    before = fish_map
    # 물고기들이 움직인다
    moveFish(eaten)

    # 이제 상어가 움직인다
    # 상어의 방향 Line 안에 들어있는 모든 물고기들을 파악한다
    # 상어의 방향 Line 은 바뀌지 않는다
    shark_pos = fishes_dict[-1]
    shark_dir = fish_map[shark_pos[0]][shark_pos[1]][1]
    avails = []
    i = 1

    while True:
        adder = [dir[shark_dir][0] * i, dir[shark_dir][1] * i]
        move_to = [shark_pos[0] + adder[0], shark_pos[1] + adder[1]]
        if move_to[0] < 0 or move_to[0] >= 4 or move_to[1] < 0 or move_to[1] >= 4:
            break

        # 해당 칸의 fish 가 없으면 안된다
        if fish_map[move_to[0]][move_to[1]][0] != 0:
            avails.append(move_to)
        i += 1

    if not avails:  # 상어가 갈 곳이 없으면 종료된다
        print("ending", eaten)
        eaten_fishes_sum.append(sum(eaten))
        return

    else:
        for target_position in avails:

            target_idx = fish_map[target_position[0]][target_position[1]][0]
            # 공통 처리요소
            # 기존 상어의 자리는 0 으로 만든다
            fish_map[shark_pos[0]][shark_pos[1]][0] = 0

            # 상어의 위치가 변경된다
            fishes_dict[-1] = [target_position[0], target_position[1]]

            # DFS 시작, 얘를 먹음
            eaten.append(target_idx)
            fish_map[target_position[0]][target_position[1]][0] = -1  # 상어가 도달
            del fishes_dict[target_idx]   # 먹이는 삭제된다

            # map 과 dict 에서 상어와 먹이에 대한 세팅
            # 상어가 떠난 자리는 0 으로 대치 (먹혔으므로)
            # 다음 DFS 로 보낸다
            dfs(eaten)

            # 다음 Loop 을 돌려야 하니, 위에서 한 것들 중 복구가 필요한건 복구시킨다

            eaten.pop()
            # 노렸던 자리에 다시 노리던 생선을 놓는다
            fish_map[target_position[0]][target_position[1]][0] = target_idx  # 상어가 도달
            fishes_dict[target_idx] = [target_position[0], target_position[1]] # 원래 타겟의 자리로 원복시킨다
'''

'''


                    o (최초)
                (한바퀴 돈다)
                (상어가 움직일 수 있는 경로)
    cur_map 전달     cur_map 전달       cur_map 전달          
        o               o                 o
(여기서 움직인다)   (여기선 다르게 움직인다)
    1마리
    ㅇ


'''
