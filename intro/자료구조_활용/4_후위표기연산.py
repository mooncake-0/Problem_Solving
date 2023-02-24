import sys

sys.stdin = open("input_4.txt")
T = int(input())

for tc in range(1, T + 1):
    line = str(input())
    stack = []
    cals = ['+', '-', '*', '/']
    for x in line:
        if x in cals:
            b = stack.pop()
            a = stack.pop()
            if x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            elif x == '*':
                stack.append(a * b)
            else:
                stack.append(a / b)
        else:
            stack.append(int(x))
    print(int(stack[0]))
# 352+*9-
# stack = 3