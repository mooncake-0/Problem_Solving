import sys

sys.stdin = open("input_2.txt")

T = int(input())
print(T)
for i in range(1, T + 1):
    rows = str(input())
    stack = []
    open_cnt = 0
    pieces = 0
    for j in range(len(rows)):
        if rows[j] == '(':
            stack.append(rows[j])
            open_cnt += 1
        else:
            if rows[j - 1] == '(':  # 바로 닫히는 것일 경우 레이저임
                stack.pop()
                open_cnt -= 1  # 바로 직전에 연 것은 빼줌
                pieces += open_cnt  # 잘려서 왼쪽 open_cnt 만큼 생성
            else: # 레이저가 아니고 그냥 닫히고 있음 # 닫힐때 생기는 조각 하나를 더해줘야함
                stack.pop()
                open_cnt -= 1
                pieces += 1
    print(pieces)
