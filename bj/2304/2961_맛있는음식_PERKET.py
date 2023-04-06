import sys

'''
포인트
- 깊이 탐색할 때 사용한 내역들 한정적인 공간이 가능하면 array 체킹이 낫다
- 왜냐면 in 조건을 사용하거면 예상치 못한 상황이 발생하기도 하고, 일단 O(N) 이기 때문이다

'''

sys.stdin = open("input_2961.txt")
input = sys.stdin.readline


def judgeTaste(used):
    global ingredients
    a_multiples = 1
    b_sums = 0
    for index in range(len(used)):
        if used[index] == 1:
            a_multiples *= ingredients[index][0]
            b_sums += ingredients[index][1]
    # for x in used):
    #     a_multiples *= x[0]
    #     b_sums += x[1]
    return abs(a_multiples - b_sums)


def takeIng(select, used, index):
    global N, values
    if sum(used) == select:
        values.append(judgeTaste(used))
    else:
        for i in range(index, N):
            if used[i] != 1:
                # if ingredients[i] not in used:  # in 조건은 O(N)이긴 함
                #     used.append(ingredients[i])
                used[i] = 1
                takeIng(select, used, i)
                used[i] = 0


def pro1():
    global N, ingredients, values
    N = int(input())
    ingredients = []  # 사용할 재료들
    values = []
    for _ in range(N):
        x, y = map(int, input().split())
        ingredients.append((x, y))

    for select in range(1, N + 1):
        takeIng(select, [0] * N, 0)

    print(min(values))


def main():
    pro1()


main()
