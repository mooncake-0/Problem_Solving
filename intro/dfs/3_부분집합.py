import sys

sys.stdin = open("input_3.txt")


def DFS(node):
    if node > num:
        if len(used_list) != 0:
            print(used_list)
        return
    else:
        used_list.append(node)
        DFS(node + 1)
        used_list.remove(node)
        DFS(node + 1)


T = int(input())

for _ in range(T):
    num = int(input())
    # num 까지의 자연수가 있는 것
    used_list = []
    DFS(1)
    print("====================")
'''
1,2,3

1 이 있냐  없냐?
2 가 있냐 없냐?
3 이 있냐 없냐? 

이런 구조로 내려가면 될 듯?

그러면 이제 한 노드가 하는 일은? 지금까지 있는 것들 모음집을 출력하는 일
'''
