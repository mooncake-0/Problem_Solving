import sys

sys.stdin = open("input_4.txt")


def DFS(index):
    if index >= len(array):
        a = sum(used_array)
        # print(used_array, "===", a)
        if a in sum_list.keys():
            sum_list[a] += 1
            return
        else:
            sum_list[a] = 1
        return
    else:
        used_array.append(array[index])
        DFS(index + 1)
        used_array.remove(array[index])
        DFS(index + 1)


T = int(input())

for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    used_array = []
    sum_list = dict()
    DFS(0)
    is_yes = False
    print(sum_list)
    for x in sum_list.values():
        if x != 1:
            is_yes = True
            break
    if is_yes:
        print("YES")
    else:
        print("NO")

