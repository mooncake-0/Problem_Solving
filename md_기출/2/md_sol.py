add = '+'
mns = '-'


def comb(chunk, n, index, no_operator):
    if sum(used) == n:
        div = divideChunks(chunk)
        if no_operator:
            judgeChunks(div)
        else:
            print(div)
            return div
    else:
        for i in range(index, len(chunk)):
            used[i] = 1
            comb(chunk, n, i + 1, no_operator)
            used[i] = 0


def divideChunks(bigChunk):
    # used index 에 따라 둘을 분할한다
    a = ""
    b = ""
    for i in range(len(bigChunk)):
        if used[i] == 0:
            a += str(bigChunk[i])
        else:
            b += str(bigChunk[i])

    return [a, b]


def judgeChunks(div):
    global cnt

    if int(div[0]) == int(div[1]):
        cnt += 1


def solution(exp):
    global used, cnt

    # exp 는 수식이 들어온다
    # 수식이 있냐 없냐가 가장 큰 기준
    used = [0] * len(exp)
    cnt = 0

    if add in exp or mns in exp:

        dividedExp = []
        a = ""
        b = ""
        index = 0
        # a = "16-+23"
        while index < len(exp):
            tmp = exp[index]
            if tmp != add and tmp != mns:
                if b != "":
                    dividedExp.append(b)
                    b = ""
                a += tmp
            else:
                if a != "":
                    dividedExp.append(a)
                    a = ""
                b += tmp
            if index == len(exp) - 1:  # 마지막 쌓아두던거 넣어놓는다
                if a != "":
                    dividedExp.append(a)
            index += 1

        red = ""
        blue = ""

        for x in dividedExp:
            if add in x or mns in x:  # 수식
                pass
            else:  # 일반식
                if len(x) > 1:
                    for chose in range(1, len(exp)):
                        comb(x, chose, 0, False) # 나뉘어진 애들이 반환된다
                else:
                    pass




    else:  # 단순히 숫자들만 있음
        for chose in range(1, len(exp)):
            # 한 명이 가질 수 있는 모든 경우의 수
            comb(exp, chose, 0, True)

        print(cnt)


a = "1111"
solution(a)
