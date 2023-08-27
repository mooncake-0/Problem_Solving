import sys

input = sys.stdin.readline
k = dict()
inside = 0
for _ in range(int(input())):
    a, b = map(str, input().split())
    if a not in k:
        k[a] = 1
        inside +=1
    else:
        del k[a]
        inside -= 1

j = list(k.keys())
j.sort(reverse=True)
for x in j:
    print(x)
