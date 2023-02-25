import sys


sys.stdin = open("input_9.txt")
T = int(input())
for _ in range(T):

    pre = input()
    pre_dict = dict()
    for x in pre:
        if x in pre_dict.keys():
            pre_dict[x] += 1
        else:
            pre_dict[x] = 1
    post = input()
    post_dict = dict()
    for x in post:
        if x in post_dict.keys():
            post_dict[x] += 1
        else:
            post_dict[x] = 1

    if pre_dict == post_dict:
        print("YES")
    else:
        print("NO")


