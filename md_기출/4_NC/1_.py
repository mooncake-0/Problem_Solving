import sys

sys.stdin = open("input_1.txt")
input = sys.stdin.readline

# N 은 100,000 까지
# integer 범위
# longet_switching slide
# 짝수 홀수 변환되어도 같은것, given 중 가장 긴 묶음
# 그냥 쭉 진해되면서 이전것과 같은지 확인해본다
def solution(A):

    #

    pass


for _ in range(int(input())):
    solution(list(map(int,input().split())))

