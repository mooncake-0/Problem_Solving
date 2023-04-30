import sys

'''
DP
> 점화식 만들기, 메모이제이션 활용하기 등에 대한 문제
> TOP - DOWN 을 통해 점화식을 분해해 나가는 방식이 많이 쓰이는듯
> BOTTOM - UP 은 점화식을 처음에 파악하는데 좋은듯 

'''

sys.stdin = open("input_1.txt")
input = sys.stdin.readline

N = int(input())


# BOTTOM-UP PROCESS
# 확인하기 쉬운 제일 작은 단위로 만들기
def pro1():
    dy = [0] * (N + 1)  # N+1 개를 만든다
    dy[1] = 1
    dy[2] = 2
    for i in range(3, len(dy)):
        dy[i] = dy[i - 1] + dy[i - 2]
    print(dy[N])


def find(num):
    global dy
    if dy[num] != 0:  # 이걸 활용해줘야 함, 안하면 30 정도만 가도 훨씬 오래걸리는 것 확인 가능
        return dy[num]
    if num == 1 or num == 2:
        return num  # 이 둘은 각각이 답임
    dy[num] = find(num - 1) + find(num - 2)
    return dy[num]


# TOP-DOWN, RECURSION, MEMOIZATION
def pro2():
    global dy
    dy = [0] * (N + 1)  # 저장공간
    print(find(N))  # num 번째 정답을 찾는다


def main():
    # pro1()
    pro2()


main()