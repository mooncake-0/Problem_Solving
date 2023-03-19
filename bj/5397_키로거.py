import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    '''
    pressed = input().strip()
    cursor = 0
    anw = []
    # 커서가 돌면서 ㅈㄹ 할 거임.
    for i in range(len(pressed)):
        if pressed[i] == '<':
            if len(anw) > 0 and cursor > 0:
                cursor -= 1
        elif pressed[i] == '>':
            if len(anw) > 0 and cursor < len(anw):
                cursor += 1
        elif pressed[i] == '-':
            if len(anw) > 0 and cursor > 0:
                cursor -= 1
                # 뒤에있는 애들을 쭉 당겨옴
                del anw[cursor]  # O(N) O(N) 을 허용하지 않으므로, 시간 초과 발생
        else:
            anw.insert(cursor, pressed[i])  # O(N)
            # 뒤에 있는 애들을 쭉 당겨옴
            cursor += 1

    for x in anw:
        print(x, end="")
    print()
    '''
    # O(N) 을 허용하지 않는다.
    # 모든 List 내부를 O(1) 로 처리하도록 함.
    # https://wiki.python.org/moin/TimeComplexity PYTHON 의 LIST 작동성에 대해서 잘 알고 있자.
    # 그리고 조금만 생각해보면 왼쪽은 list, 오른쪽은 QUEUE 를 쓰는게 올바르다는 결론이 쉽게 나옴
    # 커서 기준 왼쪽 오른쪽 생각이 어렵지만. 이미 들어버림 ㅋ
    pressed = input().strip()
    cursor = 0
    left, right = [], deque()
    for i in range(len(pressed)):
        if pressed[i] == '<':
            if left:
                right.appendleft(left.pop())
                cursor -= 1
        elif pressed[i] == '>':
            if right:
                left.append(right.popleft())
                cursor += 1
        elif pressed[i] == '-':
            if left:
                left.pop()
                cursor -= 1
        else:
            left.append(pressed[i])

    for x in left:
        print(x, end="")
    for x in right:
        print(x, end="")
    print()

