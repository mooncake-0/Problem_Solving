import sys


sys.stdin = open("input_29.txt")
input = sys.stdin.readline

N, length = map(int, input().split())

nodes = [input().strip() for _ in range(N)]

s, e = map(int, input())


'''

범위는 더 빡세지만, 
BOJ 2481 입니다


'''