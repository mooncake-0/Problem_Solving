import sys

sys.stdin = open("input_1.txt")

T = int(input())

for i in range(1, T + 1):
    num, given = map(int, input().split())
    num = list(map(int, str(num)))
    stack = []

    for x in num:
        while stack and given > 0 and stack[-1] < x:
            stack.pop()
            given -= 1
        stack.append(x)

    while given > 0:
        stack.pop()
        given -= 1
    anw = ''
    for x in stack:
        anw += str(x)
    print(anw)


    '''
    for x in str(num):
        num_list.append(int(x))
    max = -1
    biggest = []

    for i in range(len(num_list)):

        if num_list[i] > max:
            max = num_list[i]

        i = 3 // max = 7 // 4= 4 실행됨 == biggest[7], max = 6
        i =4  // max = 8 // 3 = 3 실행됨 == biggest[7,8], max = 8
        

        if len(num_list) - i == len(num_list) - given - len(biggest):
            biggest.append(max)
            max = num_list[i]

        print(biggest)
    '''
