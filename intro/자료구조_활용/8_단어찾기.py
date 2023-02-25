import sys

sys.stdin = open("input_8.txt")

T = int(input())
for _ in range(1, T + 1):
    ''' 내 풀이
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(N - 1):
        words.remove(input())
    print(words[0])
    '''
    # 강사 풀이
    N = int(input())
    p = dict()
    for i in range(N):
        word = input()
        p[word] = 1  # 해당 키값은 1의 value 로 저장

    for i in range(N - 1):
        word = input()
        p[word] = 0  # 사용했다고 지정

    for key, value in p.items():
        if value == 1:
            print(key)
