import sys

sys.stdin = open("input_6.txt")

N = int(input())
comp = []
for i in range(N):
    comp.append(list(map(int, input().split())))

comp.sort()
print(comp)
cnt = 0

for i in range(0, N):
    passed = True
    for j in range(i+1, N):
        if comp[i][1] < comp[j][1]:
            passed = False
            break
    if passed:
        cnt +=1
print(cnt)

