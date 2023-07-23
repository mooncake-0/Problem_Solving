import sys

'''
s 11:05
e 11:40
- 노가단데 살짝 아쉽.. 더 빨리할 수 있었을 것 같음
- 배열 처리하는게 너무 느렸어.. 
'''
sys.stdin = open("input_14500.txt")
input = sys.stdin.readline

I, J = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(I)]
type_1 = [[[1, 1, 1, 1]], [[1], [1], [1], [1]]]
type_2 = [[[1, 1], [1, 1]]]
type_3 = [[[1, 0], [1, 0], [1, 1]], [[1, 1, 1], [1, 0, 0]], [[1, 1], [0, 1], [0, 1]], [[0, 0, 1], [1, 1, 1]]
    , [[0, 1], [0, 1], [1, 1]], [[1, 0, 0], [1, 1, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 1, 1], [0, 0, 1]], ]
type_4 = [[[1, 0], [1, 1], [0, 1]], [[0, 1, 1], [1, 1, 0]], [[0, 1], [1, 1], [1, 0]], [[1, 1, 0], [0, 1, 1]]]
type_5 = [[[1, 1, 1], [0, 1, 0]], [[0, 1], [1, 1], [0, 1]], [[0, 1, 0], [1, 1, 1]], [[1, 0], [1, 1], [1, 0]]]
all_types = [type_1, type_2, type_3, type_4, type_5]


def check_all_num_of_figure(figure):
    tmp_i = len(figure)
    tmp_j = len(figure[0])
    max_ = -1
    for i in range(I - tmp_i + 1):
        for j in range(J - tmp_j + 1):
            tmp_sum = 0
            for k in range(len(figure)):
                for l in range(len(figure[k])):
                    if figure[k][l] == 1:
                        tmp_sum += paper[i + k][j + l]
            max_ = max(tmp_sum, max_)
    return max_


def pro1():
    anw = -1
    for type in all_types:
        for single_type in type:
            max_av = check_all_num_of_figure(single_type)
            anw = max(max_av, anw)
    return anw


def main():
    print(pro1())


main()
