import sys
K = int(input())
tmp = []
for _ in range(K):
    a = int(input())
    if a == 0:
        tmp.pop()
    else:
        tmp.append(a)
print(sum(tmp))

