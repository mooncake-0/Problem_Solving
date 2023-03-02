import sys

sys.stdin = open("input_10.txt")


def DFS(node):  # node 명시 필수 node = cur_position
    global cnt
    if node == (6, 6):
        cnt += 1
        return
    else:
        # 현재 위치에서 갈 수 있는 위치들을 파악, 단, 갔던 위치는 제외해야 함
        for i in range(4):
            mx = node[0] + dx[i]
            my = node[1] + dy[i]
            if judge_available(mx, my):
                visited.append((mx, my))
                DFS((mx, my))
                visited.remove((mx, my))


def judge_available(mx, my):
    if mx < 0 or mx > 6:
        return False
    if my < 0 or my > 6:
        return False
    if (mx, my) in visited:
        return False
    if maze[my][mx] == 1:
        return False
    return True


T = int(input())

for _ in range(T):
    maze = [list(map(int, input().split())) for _ in range(7)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    visited = [(0, 0)]
    DFS((0, 0))
    print(cnt)
