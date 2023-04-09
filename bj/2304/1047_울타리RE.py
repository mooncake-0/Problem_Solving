import sys

sys.stdin = open("input_1047.txt")
input = sys.stdin.readline

'''

문제대로 선택의 경우를 늘여놓으면 너무 많다 싶음
> 이렇게 거꾸로 생각해보는 것도 좋은듯! 
> 사실 거의 솔루션 보면서 함.. 

'''


def judge(used_idx):
    # 사각형 리스트 안에 각 used_idx 항목들로 가져오는데, 걔네들로 사각형을 만든다
    # x가 가장 큰 녀석과 작은 녀석, y 가 가장 큰 녀석과 작은 녀석을 구한다
    min_x = 1000000
    min_y = 1000000
    max_x = 0
    max_y = 0

    for k in used_idx:
        tmp = trees[k]  # x좌표, y좌표, 길이
        min_x = min(tmp[0], min_x)
        min_y = min(tmp[1], min_y)
        max_x = max(tmp[0], max_x)
        max_y = max(tmp[1], max_y)

    rec_length = 2 * (max_x - min_x) + 2 * (max_y - min_y)

    l = 0
    cnt = 0

    tmp = []

    # 범위가 나왔고, trees 를 돌려주면서 가능한 애들과 불가능한 애들은 선별하며, 길이를 구하고, 저 사각형으로 되는지 판단한다
    for i in range(len(trees)):
        # k 범위 밖에 있으면 무조건 자르는거다
        # 그리고 k 안에 있는 애들중에 가장 높은 길이를 가진 애를 순서대로 자르면서 더해졌을 때 가능한지 판별한다
        # 끝까지 안될 수도 있음
        k = trees[i]
        if min_x <= k[0] <= max_x and min_y <= k[1] <= max_y:
            # 범위 안에 있는 애들을 동시에 하면, 밖에 있는 애들을 고려하지 못한 결론이 나온다.
            tmp.append(i)
        else:
            l += k[2]
            cnt += 1


    if rec_length > l:  # 해결안되므로, 범위 안에 있는 (기준선 외) 애들을 자르면서 돌려본다
        # 뒤쪽이 나무 많은 애임
        while tmp:
            idx = tmp.pop()
            if idx not in used_idx: # 기준이 되는 애를 가지고 생각해야 함
                # 얘를 쓸거임
                l += trees[idx][2]
                cnt +=1

                if rec_length <= l:
                    return cnt
        # 여기까지도 안되면, 얘는 걍 안되는 거
        return -1
    else: # 여기서 해결되면 굳
        return cnt


def combination(n, used):
    global cnt, min_trees
    if len(used) == n:
        # used 에는 4가지 idx 가 들어 있고, 이 idx 들 기준으로 사각형을 만든다
        is_av = judge(used)
        if is_av > 0:
            min_trees = min(is_av, min_trees)
    else:
        for i in range(len(trees)):
            used.append(i)
            combination(n, used)
            used.pop()


N = int(input())

trees = []

for _ in range(N):
    *tree_pos, t_l = map(int, input().split())
    trees.append((tree_pos[0], tree_pos[1], t_l))

# 나무 많은 순이 뒤에 오도록 정렬해 놓는다
trees.sort(key=lambda x: x[2])

min_trees = 40
combination(4, [])
print(min_trees)
# 직사각형을 먼저 만들고, 그 안에 들어오는 애들은 선별한다 *40
# 선별된 애들의 T,F 를 판별하고, T 라면 잘려야 하는 나무의 갯수를 최저인 녀석으로 지속 업데이트를 해준다.
# 업데이트 최종본을 반환한다
