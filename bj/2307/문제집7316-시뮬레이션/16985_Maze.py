import sys
from collections import deque

'''
포인트
- 나는 시간이 너무 오래 걸림. 한문제 한문제가.
- 물론 많이 풀면 풀수록 빨라지겠지만..
- 중복, 순열, 조합 같은거 사용하는건 그냥 외워놓는게 좋을 듯
- 그냥.. 노가다 문제였음
'''

sys.stdin = open("input_16985.txt")
input = sys.stdin.readline

# 5*5 크기 판 5개
plates = []
for _ in range(5):
    tmp = [list(map(int, input().split())) for _ in range(5)]
    plates.append(tmp)

dk, di, dj = [0, 0, 0, 0, 1, -1], [0, 1, 0, -1, 0, 0], [1, 0, -1, 0, 0, 0]


def rotate_single(rotatee):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[i][j] = rotatee[j][4 - i]
    return tmp


def rotate_plate(plate):
    anws = []
    anws.append(plate[:])  # 자기자신
    for _ in range(3):
        plate = rotate_single(plate)
        anws.append(plate[:])
    return anws


def do_dup_dfs(tmp, combinations):
    if len(tmp) == 5:
        combinations.append(tmp[:])
    else:
        for i in range(4):
            tmp.append(i)
            do_dup_dfs(tmp, combinations)
            tmp.pop()


# 중복조합 idx 묶음 반환
def comb_dup_av():
    combinations = []
    do_dup_dfs([], combinations)
    return combinations


def line_up_dfs(tmp, chosen, combinations):
    if len(tmp) == 5:
        combinations.append(tmp[:])
    else:
        for i in range(5):
            if i not in chosen:
                tmp.append(i)
                chosen.add(i)
                line_up_dfs(tmp, chosen, combinations)
                tmp.pop()
                chosen.remove(i)


def comb_line_up():  # 순열 반환
    combinations = []
    line_up_dfs([], set(), combinations)
    return combinations


# 층, i, j
# (0,0,0) -> (4,4,4)
# (0,4,0) -> (4,0,4)
# (0,0,4) -> (4,4,0)
# (0,4,4) -> (4,0,0)

def search_maze(single_set):
    start_cand = []

    if single_set[0][0][0] == 1:
        start_cand.append((0, 0, 0))
    if single_set[0][4][0] == 1:
        start_cand.append((0, 4, 0))
    if single_set[0][0][4] == 1:
        start_cand.append((0, 0, 4))
    if single_set[0][4][4] == 1:
        start_cand.append((0, 4, 4))

    cur_min = 5 * 5 * 5 * 10

    for start in start_cand:

        start_pos = start
        dq = deque()
        dq.append((start, 0))

        visited = set()
        visited.add(start)

        while dq:

            cur_position, times = dq.popleft()
            if start_pos == (0, 0, 0) and cur_position == (4, 4, 4):
                cur_min = min(times, cur_min)
                break
            elif start_pos == (0, 4, 0) and cur_position == (4, 0, 4):
                cur_min = min(times, cur_min)
                break
            elif start_pos == (0, 0, 4) and cur_position == (4, 4, 0):
                cur_min = min(times, cur_min)
                break
            elif start_pos == (0, 4, 4) and cur_position == (4, 0, 0):
                cur_min = min(times, cur_min)
                break

            for t in range(6):
                mk = cur_position[0] + dk[t]
                mi = cur_position[1] + di[t]
                mj = cur_position[2] + dj[t]

                if 0 <= mi < 5 and 0 <= mj < 5 and 0 <= mk < 5 and (mk, mi, mj) not in visited and single_set[mk][mi][mj] == 1:
                    dq.append(((mk, mi, mj), times + 1))
                    visited.add((mk, mi, mj))

    return cur_min


def remove_duplicate(all_set):
    global tmp_set
    for one_cube in all_set:
        tmp_cube = []
        for one_plate in one_cube:
            tmp_plate = []
            for one_line in one_plate:
                tmp_plate.append(tuple(one_line))
            tmp_cube.append(tuple(tmp_plate))
        tmp_set.add(tuple(tmp_cube))


'''
1번 PARAM - 4^5 조합 idx 들
2번 PARAM - 탑 쌓기 120개 조합 idx 들
'''


def build_all_possible(plate_idx_comb, build_cube_comb):
    global tmp_set
    rotated_tmp = []
    for x in plates:
        plate_rotated = rotate_plate(x)  # 한 plate 이 회전한 4개를 반환한다
        rotated_tmp.append(plate_rotated)

    one_set = []
    for idxs in plate_idx_comb:  # 사용할 plate 들의 idx 들
        tmp = []
        for i in range(5):
            tmp.append(rotated_tmp[i][idxs[i]])
        one_set.append(tmp)

    # one : plate 당 4가지 회전을 할 수 있는데, 각 plate 들의 회전 상황을 고려한 한 set
    all_set = []
    for one in one_set:  # 4가지 고른 애들 중
        for idx_set in build_cube_comb:
            cube = []
            for idx in idx_set:
                cube.append((one[idx]))
            all_set.append(cube)

    anw = 5 * 5 * 5 * 10

    tmp_set = set()
    remove_duplicate(all_set)

    # 이제 탑을 돌면서 BFS 를 하자..
    for single_set in tmp_set:
        k = search_maze(single_set)
        anw = min(k, anw)

    if anw == 5 * 5 * 5 * 10:
        print(-1)
    else:
        print(anw)


def main():
    plate_idx_comb = comb_dup_av()
    build_cube_comb = comb_line_up()
    build_all_possible(plate_idx_comb, build_cube_comb)


main()
