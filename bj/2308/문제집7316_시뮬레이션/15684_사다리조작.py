import sys

'''
포인트
 - 쭉 했으면 두시간 반정도 걸렸을 듯 
 - itertools -> list 로 반환하는 시간까지 있음 (그냥 중복, 순열, 조합 외우는게 나을 듯 - 내가 직접 제어 가능) 
 - 그리고 첫 parse 함수는 굳이 그 list 를 한번 더 돌면서 제거를 함
 - 나중에 어차피 돌 때 확인해보면 시간이 더 절약됨. 
 - 한 단위지만, 한단위 자체가 3천~5천 정도라, 절약 되는게 맞음
 - 좀 많이 찝찝한 문제 
 - 처음에 노가다성이 맞는지 계산 후 진입하는건 필요함. dict 전후 로직으로 확인해 가는것도 ㄱㅊ았던 부분
'''

sys.stdin = open("input_15684.txt")
input = sys.stdin.readline

J, line_cnt, I = map(int, input().split())
linked_dict = dict()
mover_set = set()

for j in range(1, J + 1):
    td = dict()
    linked_dict[j] = td

for _ in range(line_cnt):
    b, a = map(int, input().split())
    mover_set.add((a, a + 1, b))
    linked_dict[a][b] = a + 1
    linked_dict[a + 1][b] = a

empties = []  # idx~ idx+1 이 k 번째 줄에서 (idx, k) 로 저장

for i in range(1, I + 1):
    for j in range(1, J):
        if (j, j + 1, i) not in mover_set:
            if j > 1 and (j - 1, j, i) in mover_set:
                continue
            if j < J - 1 and (j + 1, j + 2, i) in mover_set:
                continue
        else:
            continue
        # 다 통과 시 들어올 수 있음
        empties.append((j, i))

# run 함수 필요 - 돌렸을 때 i 번째가 어디로 가는지 반환한다
# 하나씩 추가하면서, 하나 추가했을 경우의 모든 상황을 한번더 판단한다
# 두개씩 추가 - 모든 Combination 계산 필요
# 세개 추가 - 모든 Combination 계산 필요 - 이게 제일 Hard Logic 일듯
# I = 30 , J =10 (I-1 * J 개의 다리 가능) = 29 * 10
# 최대 약 2천~ 5천?
def check_next_cross(cur_idx, cur_depth):  # cur_idx 에서 내려갈 때 이동해야 하는 다음 사다리를 찾느다
    linked = linked_dict[cur_idx]
    for i in range(cur_depth + 1, I + 1):
        if i not in linked:
            continue
        return (i, linked[i])  # i 번째에서 linked[i] 와 연결되어 있음
    # 연결된게 없다면 바로 cur_idx 반환한다
    return -1


def run(idx):  # 해당 i 번이 사다리를 탈 것이다. 결과를 반환해보자
    cur_depth = 0
    cur_idx = idx
    while cur_depth < I:  # 끝날때까지 돌지 않는다
        anw = check_next_cross(cur_idx, cur_depth)
        if anw == -1:
            return cur_idx
        # 그 칸으로 가야함
        cur_depth = anw[0]
        cur_idx = anw[1]
    return cur_idx


def judge_anw():
    is_av = True
    for num in range(1, J + 1):
        if num != run(num):  # 하나라도 있다면
            is_av = False
            break  # 그만해도 됨
    return is_av


def not_work(chunk):
    for i in range(len(chunk)):
        for j in range(i + 1, len(chunk)):
            if chunk[i][1] == chunk[j][1]:  # 같은 층에서
                if abs(chunk[i][0] - chunk[j][0]) == 1:  # 인접해 있다면
                    return False
    return True


def combination(cnt, depth, cur_chosen, l):
    global chosen
    if depth == cnt:
        chosen.append(cur_chosen[:])
    else:
        for k in range(l, len(empties)):
            cur_chosen.append(empties[k])
            combination(cnt, depth+1, cur_chosen, k+1)
            cur_chosen.pop()

def pro1():
    global linked_dict, chosen
    cnt = 0

    while cnt < 4:
        chosen = []
        combination(cnt, 0, [], 0)

        if len(chosen) == 0:

            if cnt == 0:  # 처음이라면
                hi = judge_anw()
                if hi:
                    return cnt
                else:
                    cnt += 1
            else:
                return -1

        else:
            for x in chosen:  # 걔를 더했다가, 다시 빼준다
                t = not_work(x)
                if not t:
                    continue

                for add in x:  # add[0] 과 add[0] +1 이 add[1] 번째에서 연결된다
                    linked_dict[add[0]][add[1]] = add[0] + 1
                    linked_dict[add[0] + 1][add[1]] = add[0]
                hi = judge_anw()
                for add in x:  # 바로 원복시킨다
                    del linked_dict[add[0]][add[1]]
                    del linked_dict[add[0] + 1][add[1]]

                if hi:
                    # 성공을 했다면 그만해도 된다
                    return cnt
            cnt += 1
    return -1


def main():
    print(pro1())

main()
