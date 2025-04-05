import sys


sys.stdin = open("input_2.txt")
input = sys.stdin.readline

def solution(Board):
    for x in Board:
        print(x)
    pass

A =[[9,1,1,0,7],[1,0,2,1,0], [1,9,1,1,0]]
solution(A)