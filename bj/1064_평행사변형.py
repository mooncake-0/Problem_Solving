import sys

sys.stdin = open("input.txt")

x1, y1, x2, y2, x3, y3 = map(int, input().split())

#평행일 경우 제외
if (y3-y2)*(x2-x1) == (x3-x2)*(y2-y1):
    print(-1)

else:
    aLen = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    bLen = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    cLen = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5


    round_list = []

    round_list.append(2*(aLen + bLen))
    round_list.append(2*(aLen + cLen))
    round_list.append(2*(cLen + bLen))

    print(max(round_list) - min(round_list))