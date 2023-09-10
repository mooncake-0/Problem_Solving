import sys

sys.stdin = open("input_1560.txt")

n = int(input())
if n <=2 :
    print(n)
else :
    print(n + (n-2))