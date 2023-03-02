import sys

sys.stdin = open("input_6.txt")


def DFS(node, anw):  # node = current index
    global cnt
    if node >= len(str(encrypt)):
        cnt += 1
        print(anw)
        return
    else:
        if int(str(encrypt)[node]) != 0:
            anw += chr(int(str(encrypt)[node]) + 64)
            DFS(node + 1, anw)
            anw = anw[:len(anw) - 1]
            if 26 >= int(str(encrypt)[node:node + 2]) >= 10:
                anw += chr(int(str(encrypt)[node:node + 2]) + 64)
                DFS(node + 2, anw)


T = int(input())

for _ in range(T):
    encrypt = int(input())
    # AB ~ XYZ 까지 알파벳 == 그 수
    cnt = 0
    DFS(0, "")
    print(cnt)

# 115213102120131
# 35561010212013105164112032121321214
# 1556101021201310516411203212132
