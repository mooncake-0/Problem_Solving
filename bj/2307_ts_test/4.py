import sys

sys.stdin = open("input_4.txt")
input = sys.stdin.readline


def select_k_tuples(arr, k):
    tuples = []
    select_tuples_recursive(arr, k, [], tuples)
    return tuples

def select_tuples_recursive(arr, k, current_tuple, tuples):
    if k == 0:
        tuples.append(current_tuple)
        return
    if len(arr) < k:
        return
    select_tuples_recursive(arr[1:], k, current_tuple + [arr[0]], tuples)
    select_tuples_recursive(arr[1:], k - 1, current_tuple, tuples)

def solution(prices, k):
    a = select_k_tuples(prices, k)
    for x in a:
        print(x)


prices = list(map(int, input().split()))  # 7 ~ 100
k = int(input())  # k 3 ~ 500
# 적어도 k+1 일 전에는 매수 필요
print(solution(prices, k))
