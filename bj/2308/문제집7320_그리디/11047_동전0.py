import sys

sys.stdin = open("input_11047.txt")
input = sys.stdin.readline

N, K = map(int, input().split()) # N - 갯수, K - 합원 # N ~ 10
coins =[]
for _ in range(N):
    coins.append(int(input()))

def pro1():
    cnt = 0
    cur_sum =0
    while cur_sum < K:
        if cur_sum > K:
            print("이럴리없음")
            break
        tmp = coins.pop()
        while cur_sum + tmp <= K:
            cur_sum += tmp
            cnt += 1
    return cnt

def main():
    print(pro1())



main()
