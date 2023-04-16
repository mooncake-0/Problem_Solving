import sys

sys.stdin = open('input_13706.txt')  # 제출시에는 주석or제거
input = sys.stdin.readline

N = int(input())
s = 1
e = N

''' O(log (e-s))   : log(e) < 32 '''
while s <= e:
    mid = (s + e) // 2
    print(s, mid, e)
    if mid * mid <= N:  # 조건 만족
        s = mid + 1
    else:
        e = mid - 1

print(e)