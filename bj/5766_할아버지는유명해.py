import sys

sys.stdin = open("input_5766.txt")

while True:

    player = [[0,i] for i in range(10001)]
    N,M = map(int, input().split())

    if N and not M:
        break

    for _ in range(N):
        for n in map(int, input().split()):
            player[n][0] += 1

    player.sort(reverse=True, key = lambda x: [x[0], -x[1]])

    player2_score = player[1][0]
    player2_place = [player[1][1]]

    for i in range(2, 10001):
        if player[i][0] == player2_score:
            player2_place.append(player[i][1])
        else:
            break

    print(*player2_place)
