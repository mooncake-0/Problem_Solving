'''
G1에 속한 시청자가 후원한 도네이션 각각에 C%의 세금이 붙는다.

G2에 속한 시청자가 후원한 도네이션 각각에는 세금이 붙지 않는다.

'''

'''
다만, 그 도네이션들을 모두 종합하여 D × |G2|**2 원의 세금을 내야 한다.

교준이가 세금을 제한 후 받을 수 있는 최대 환전 금액
'''


# n => int 도네이션 횟수
# c => G2 에 붙는 세금 %
# d => D*100
# a => 시청자 Ai
# b => 시청자별 후원 금액 Bi

# G1에 속한 시청자가 후원한 도네이션 각각에 C%의 세금이 붙는다.
def tax_g1(g1):
    global c_, b_
    if not g1:
        return 0
    p = c_/ 100

    tax = 0
    for index in g1:
        tax += b_[index] * p
    return tax

'''
G2에 속한 시청자가 후원한 도네이션 각각에는 세금이 붙지 않는다.
다만, 그 도네이션들을 모두 종합하여 D × |G2|**2 원의 세금을 내야 한다.
'''
def tax_g2(g2):
    global d_, b_
    if not g2:
        return 0
    D = d_/100
    sum_g2 = 1
    for index in g2:
        sum_g2 *= b_[index]

    return D*(sum_g2**2)




def judge_each(g1, g2): # 각 세금의 합을 구해, 최대치를 계산한다
    global taxes
    total_tax_g1 = tax_g1(g1)
    total_tax_g2 = tax_g2(g2)
    taxes.append(total_tax_g1+total_tax_g2)


def divide(ppl):
    g1 = []
    g2 = []
    for i in range(len(ppl)):
        if ppl[i] == 0:
            g1.append(i)
        else:
            g2.append(i)
    judge_each(g1,g2)



def comb(lim, index):
    global ppl
    if sum(ppl) >= lim:
        divide(ppl)
        return

    for i in range(index, len(ppl)):
        ppl[i] = 1
        comb(lim, i + 1)
        ppl[i] = 0


## N = 100,000 ..
# 이름은 신경안써도 될 듯 해 보임
def solution(n, c, d, a, b):
    global ppl, c_, d_, b_, taxes

    c_ = c
    d_ = d
    b_ = b
    ppl = [0] * n
    # print(ppl)

    # 0 명부터 n 명까지 선택이 분할되는 모든 경우의 수
    taxes =[]
    for x in range(n+1):
        comb(x, 0)

    # 다 돌고 나면 taxes 에 모든 값들이 들어가 있음
    tax = min(taxes)
    return int((sum(b) - tax)*100)

n = 2
c = 100
d = 10
a, b = ["fan", "Fan"], [1,2]
print(solution(n,c,d,a,b))
