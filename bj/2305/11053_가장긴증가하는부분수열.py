import sys

input = sys.stdin.readline


# N < 1000
# A < 1000

def bup():
    global each_longest, N
    # 10 ~ 50 중
    # 10 밖에 없음
    # 10 1개
    # 10 20 있음
    # 10 20 1 개
    # 10 20 10 있음 (끝에 무조건 10)
    # 그 앞에 증가하는 애가 없기 때문에, 1 임
    # 1
    # 10 20 10 30
    # 10 20 10 30 인데,30은 앞에있는 애들이 모두 된다. 따라서, 지금까지 앞에 나온 것중에 가장 긴 값 + 1 이 30의 값
    each_longest[1] = 1
    # ...
    for i in range(2, len(each_longest)):  # 6까지
        # 지금까지 나온 길이중 제일 긴 길이
        # 하지만 지금까지 나온 길이중, 자기보다 작은 값일 경우에만 해당한다
        # 즉,
        max_l = 1 # 기본적으로 자기 혼자만 될 수 있으므로, 1일 것임
        # 앞에서부터 쭉 탐색한다
        for j in range(1, i+1): # 현재 자신 위치까지 오면서 파악을해봄
            if nums[j] < nums[i]: # 나보다 작음 ( 증가 방향이 맞음 )
                max_l = max(max_l, each_longest[j] + 1) # 해당의 가장 긴 값보다 +1 해줌
        each_longest[i] = max_l

    return max(each_longest)


def main():
    global nums, each_longest, N
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    each_longest = [0] * (N + 1)
    if N == 1:
        print(1)
    else:
        print(bup())


main()
