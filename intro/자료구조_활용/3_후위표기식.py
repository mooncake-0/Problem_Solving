import sys

###### 개인적으로 너무 어려웠던 문제 ####### 아직도 못풀겠음

sys.stdin = open("input_3.txt")

T = int(input())

for _ in range(1, T + 1):
    line = input()
    stack = []
    anw = ''
    for x in line:
        if x.isdecimal():  # 숫자일 경우 누적시킨다
            anw += x
        else:  # 연산자이다
            if x == '(':
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    # 그 전에 현재 있는 연산을 모두 끝낸다
                    anw += stack.pop()
                # 이제 바로 앞에 ( 가 있을테니까 끄집어낸다,
                stack.pop()
            elif x == '*' or x == '/':  # stack 이 비어있지 않고, stack 의 상단이
                while stack and (stack[-1] == '*' or stack[-1] == '/'):  # 같은 우선순위의 자료를 먼저 처리한다.
                    anw += stack.pop()
                # 앞에 있는지만 확인하고, 자기가 들어간다
                stack.append(x)
            else:
                while stack and stack[-1] != '(':  # 빼다가 여는 괄호를 만났다면, 지금 돌고 있는 +,- 는 괄호 안의 연산이다
                    anw += stack.pop()
                stack.append(x)

    # stack 에 남아있는 애들 조진다
    while stack:
        anw += stack.pop()
    print(anw)

    '''
    prior = ['*', '/']
    minor = ['+', '-']
    needsCal = False
    for x in line:
        if x in prior or x in minor:
            if x in minor:
                stack.append(x)
            else: # 우선 계산이니 써야함
                needsCal = True
                stack.append(x)
        elif x == '(' or x == ')': # 모든 상황을 종료하고 괄호 안에 집중한다
            bracket_cal = ''
            if x == '(':
                stack.append(x)
            else:


        else:
            anw.append(x)
            if needsCal:
                anw.append(stack.pop())
                needsCal = False
        '''
