import sys

sys.stdin = open("input_15683.txt")
input = sys.stdin.readline

# 6 벽
# 1 한 쪽, 2 180, 3 90, 4 270, 5 360

I, J = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(I)]

# 각 CCTV의 방향벡터들
d_1 = [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]]
d_2 = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
d_3 = [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]]
d_4 = [[(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)]]
d_5 = [[(0, 1), (0, -1), (1, 0), (-1, 0)]]


def temp(vectors, cur_position):
    new_candidates = []
    for x in vectors:  # 이거 하나가 한 후보
        candidate = set()
        for dir in x:  # 여기 안에 있는 것들은 동시에 한 후보들이다.
            times = 1
            while True:
                mi = cur_position[0] + dir[0] * times
                mj = cur_position[1] + dir[1] * times

                if 0 > mi or I <= mi or 0 > mj or J <= mj:
                    break

                if room[mi][mj] == 6:
                    break

                # 다 통과한다면 ㄱㄴ 한것이므로, 후보가 된다.
                candidate.add((mi, mj))
                times += 1
        new_candidates.append(candidate)

    return new_candidates


# 그리고 set 크기가 가장 큰 걸로 결정된다
# 예를 들어, 1을 통해 Choices 에 4가지가 들어왔음
# 그리고 그 다음이 2를 통해 2가지 choice 가 추가된다면, 8가지 choice 가 있는거임
# CCTV 최대 갯수는 8개 이므로 1로 꺾으면 4^8 = 최대 약 60000개 > 할만함
# 최적 길이를 그 때 그 떄 하지 말고, 차라리 HEAP 으로 하면, 제일
def judge_candidate(cctv_position):
    # cctv 종류별로, 가능한 방향, 해당 방향 내의 cover 가능한 애들을 판단해서, 추가한다
    type = room[cctv_position[0]][cctv_position[1]]

    if type == 1:  # 4가지 경우 생성
        new_candidates = temp(d_1, cctv_position)
    if type == 2:  # 2가지 경우 생성
        new_candidates = temp(d_2, cctv_position)
    if type == 3:  # 2가지 경우 생성 (90도)
        new_candidates = temp(d_3, cctv_position)
    if type == 4:  # 3가지 경우 생성
        new_candidates = temp(d_4, cctv_position)
    if type == 5:  # 4가지 경우 생성
        new_candidates = temp(d_5, cctv_position)

    for x in new_candidates:
        x.add(cctv_position)

    # print(new_candidates)

    cross_candidates(new_candidates)



def cross_candidates(new_candidate):
    global candidates

    if not candidates:
        for x in new_candidate:
            candidates.append(x)
    else: # 여기선 하나씩 cross 해야함
        new_candidates= []
        for x in candidates:
            for j in new_candidate:
                new_set = x.union(j)
                new_candidates.append(new_set)
        candidates = new_candidates



def pro1():
    global max_val, candidates
    max_val = -1
    candidates = []  # 후보군들에 대한 set 집합들
    total_block = I * J
    for i in range(I):
        for j in range(J):
            if room[i][j] != 0 and room[i][j] != 6:
                judge_candidate((i, j))
            if room[i][j] == 6:
                total_block -= 1

    for x in candidates:
        max_val = max(max_val, len(x))

    if max_val == -1:
        max_val = 0
    print(total_block-max_val)


def main():
    pro1()


main()
