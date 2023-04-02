add = '+'
mns = '-'


def comb(chunk, n, index, no_operator):
    if sum(used) == n:
        div = divideChunks(chunk)
        if no_operator:
            judgeChunks(div)
        else:
            print(div)
            return
    else:
        for i in range(index, len(chunk)):
            used[i] = 1
            comb(chunk, n, i + 1, no_operator)
            used[i] = 0


def divideChunks(bigChunk):
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

    used = [0] * len(exp)
    cnt = 0

    if add in exp or mns in exp:
        dividedExp = []
        a = ""
        b = ""
        index = 0
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
            if index == len(exp) - 1:
                if a != "":
                    dividedExp.append(a)
            index += 1

        for x in dividedExp:
            if add in x or mns in x:
                pass
            else:
                if len(x) > 1:
                    for chose in range(1, len(exp)):
                        comb(x, chose, 0, False)
                else:
                    pass
        return None

    else:  # 단순 숫자
        for chose in range(1, len(exp)):
            comb(exp, chose, 0, True)
        return cnt

a = "1111"
solution(a)
