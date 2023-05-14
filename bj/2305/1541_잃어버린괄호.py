# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들어라
# 첫줄 : 0~9, +, - 만으로 이루어짐 / 가장 첫, 마지막 문자는 숫자.
# 식의 길이 <50
# 5자리보다 많이 연속되는 숫자는 없다? 111111 이런거 안된다는 뜻인듯
# 55 - 50 + 40
# - 에서 - 사이는 모두 괄호를 쳐준다 = + 들을 더해서 아래로 내려준다
import sys

sys.stdin = open("input_1541.txt")
input = sys.stdin.readline


def pro1(eq):
    # eq 를 가지고 내가 세운 가정을 기반으로 푼다
    # 계산을 해나간다 > - 가 등장하면 다음이 연산이 - 인지 + 인지 판단한다 . + 면 괄호연산을 실행한다
    anw = 0
    current_eq = '+'
    is_bracket = False
    for i in range(len(eq)):
        if eq[i] != '+' and eq[i] != '-':  # 숫자임
            if current_eq == '+':
                anw += int(eq[i])
            else:
                anw -= int(eq[i])

        else:  # 연산식임
            if eq[i] == '+':  # is_bracket 일 경우 빼준다
                if is_bracket:
                    current_eq = '-'
                else:
                    current_eq = '+'
            else:  # '-' 일 경우
                if i < len(eq) - 2:
                    if eq[i + 2] == '+':  # 자신의 다다음 것
                        is_bracket = True
                    else:
                        is_bracket = False
                current_eq = '-'
    print(anw)


def main():
    line = input().strip()
    tmp = ''
    eq = []
    for x in line:
        if x != '+' and x != '-':
            tmp += x
        else:  # 지금까지 저장한 수를 저장, + 혹은 - 저장
            eq.append(tmp)
            eq.append(x)
            tmp = ''
    eq.append(tmp)
    pro1(eq)


main()
