import sys

input = sys.stdin.readline

'''
보기를 보고 깨달은 문제
'''

## 틀림 -> 25974 .. 꼭 정렬된 상태에서 하나씩 바꾸는거가 틀린 판단
def findSmallestDiffWRONG(logs):
    logs.sort()
    cur_score = logs[-1] - logs[0]  # 가장 큰 값
    # 자리를 바꾸고, 바꾸면서 변한 값들에 중 제일 큰 값을 비교, 그게 더 작으면 최신화!
    for i in range(1, len(logs) - 1):
        logs[i], logs[len(logs) - 1] = logs[len(logs) - 1], logs[i]  # 바꿔봄
        std = -1
        if abs(logs[i] - logs[i - 1]) > std:
            std = abs(logs[i] - logs[i - 1])
        if abs(logs[i] - logs[i + 1]) > std:
            std = abs(logs[i] - logs[i + 1])
        if abs(logs[len(logs) - 1] - logs[len(logs) - 2]) > std:
            std = abs(logs[len(logs) - 1] - logs[len(logs) - 2])
        if abs(logs[len(logs) - 1] - logs[0]) > std:
            std = abs(logs[len(logs) - 1] - logs[0])
        # 가장 차이가 큰 녀석으로 기록됨
        print(cur_score, std)
        if cur_score > std:
            cur_score = std
        # 다시 바꿔줘야 한다
        logs[i], logs[len(logs) - 1] = logs[len(logs) - 1], logs[i]  # 원복
    print(cur_score)


# 정답
def spreadFromSmallest(N, logs):
    # N 만큼의 배열을 미리 만들어 둔다
    smallest = [-1] * N
    logs.sort()
    # logs 에서 하나씩 앞뒤로 말면서 배치
    # 짝수인 경우 -> 하나씩 말면서 잘 배치 됨
    if N // 2 == 0:
        for i in range(0, N // 2):
            smallest[i] = logs[2 * i]
            smallest[N - 1 - i] = logs[2 * i + 1]
    else:
        for i in range(0, N // 2):
            smallest[i] = logs[2 * i]
            smallest[N - 1 - i] = logs[2 * i + 1]
        smallest[N // 2] = logs[N - 1]

    # 이제 가장 큰 연이은 수를 찾는다
    biggest = abs(smallest[0] - smallest[1])
    for i in range(len(smallest) - 1):
        if biggest < abs(smallest[i] - smallest[i + 1]):
            biggest = abs(smallest[i] - smallest[i + 1])
    if biggest < abs(smallest[len(smallest) - 1] - smallest[0]):  # 마지막 것도 판단
        biggest = abs(smallest[len(smallest) - 1] - smallest[0])
    print(biggest)


TC = int(input())

for _ in range(TC):
    N = int(input())
    logs = list(map(int, input().split()))
    spreadFromSmallest(N, logs)
