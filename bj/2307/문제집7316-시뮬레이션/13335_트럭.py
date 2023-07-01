# n 개의 트럭이 건넌다.
# w 대만 동시에 올라갈 수 있다.
# 트럭들의 무게의 합은 최대하중인 L보다 작거나 같아야 한다.
import sys

sys.stdin = open("input_13335.txt")
input = sys.stdin.readline
# n,w, L ~ 1000
N, W, L  = map(int, input().split())
trucks = list(map(int,input().split()))

# 묶음을 찾는다면, 시간 계산은 따로 계산할 수 있다.
# 적합한 묶음을 찾는 것이 우선
# list 중 총합이 L 혹은 갯수가 W 를 넘지 않는 선에서 계속 자른다

def pro1():
    pass

def main():
    pro1()

main()