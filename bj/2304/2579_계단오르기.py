import sys

input = sys.stdin.readline

# 방금 전 문제로 계단 오르기는 피보나치임을 알 수 있었음
# 하지만 여기서는 경로가 중요함
# 각 오름마다 생길 수 있는 점수들을 파악해야함
'''
포인트
    - 아 너무 어려웠음.. 진짜로..
    - 철저히 "나" 기준에서 생각하는 것 >> MAX_SCORE 저장과 진행중인 SCORE 이 철저한 분리
    - 현재 "나" 까지 올라올 수 있는 경우를 생각하는 것
    - MAX_SCORE 에 저장했다는 것은 그 경로를 채택했다는 것은 맞는 말이다. 
    - 따라서 현재 나한테까지 올 때, MAX_SCORE 을 사용하려면, 그 경로가 사용되었을 수 있다는 점을 고려해야 하는건 맞는 포인트
                    >> 난 여기서 혼자 너무 꼬여서 생각하느라 실패
    - 내 문제는 이것이였음
    - I 위치까지 올라올 때, I-1 을 통해 올라온 경우가 채택된다면 MAX_SCORE[I] 에 그렇게 저장될 것
    - 하지만, MAX_SCORE[I+1] 을 계산할 때는, MAX_SCORE[I] 까지 I-1 을 통해 올라왔다면, I를 통해 올라가는 경우의 수가 제외되어야 한다 
    - 그래서 I-3 이 등장하는 것
    - 나의 Max_score 를 계산할 때는, MAX_SCORE[I-2] 에서 +2 로 올라오는 경우의 수와
                                  MAX_SCORE[I-3] 에서 +2 해서 I-1 로 올라왔고, 그 다음에 +1 로 I로 오는 것
                                  -> 이렇게 된다면, I-1 까지 올라온 경우의 수는 +2 였고, 나한테까지 올대 +1 을 쓴다
                                  -> 그리고 MAX_SCORE[I] 에 이 경로가 채택된다면
                                  -> MAX_SCORE[I+1] 에는 이 경로가 생각되면 안된다. 
                                  -> 그래서 생각안함 >> MAX_SCORE 를 계산하는동안 MAX_SCORE[I-1] 은 사용되지 않기 때문임.
                                  -> 다 다른경로임. Max_SCORE[I+1] 을 계산할 때, MAX_SCORE[I] 까지의 경로를 고려하지 않는다
                                  -> MAX_SCORE[I-1] 에서 +2 로 올라오는 경로는 고려가 되지만, (MAX[I-2] 는 사용되기 때문)
                                  -> MAX_SCORE[I] +1 의 경로는 사용되지 않음
                                  -> MAX_SCORE[3] 에서 +2 +1 로 왔을 경우만!! 생각함 > 이 경로만이 고려됨
                                  > I 에서 올라오는 경로는, 반드시 MAX_SCORE[I-3] 에서 올라왔어야만 한다고 명시해준 셈
    > 아직 아리송 하지만, 그런 것 같음.                       
'''


# 아 너무 어려웠음.. 진짜로..
# 철저히 "나" 기준에서 생각하는 것

# BUP
def pro1():
    global N, max_scores
    max_scores[1] = scores[1]
    max_scores[2] = scores[1] + scores[2]
    max_scores[3] = max(scores[1] + scores[3], scores[2] + scores[3])
    # I-3 까지 등장하기 때문에, 3 까지 조건에 넣어준다
    for i in range(4, len(max_scores)):
        # 두 경로중 큰 값일 뿐
        max_scores[i] = max(max_scores[i - 2] + scores[i], max_scores[i - 3] + scores[i - 1] + scores[i])
    print(max_scores[N])


# 계단 오르는중
# 1 - 1
# 2 - 1+1 / 2
# 3 번째까지는 1+2 / 2+1

def main():
    global N, scores, max_scores
    N = int(input())
    scores = [0] * (N + 1)
    max_scores = [0] * (N + 1)
    for idx in range(1, len(scores)):
        scores[idx] = int(input())

    if N <= 3:  # max_score, score 모두 3까지밖에 없음
        if N == 1:
            print(scores[1])
        if N == 2:
            print(scores[1] + scores[2])
        if N == 3:
            print(max(scores[1] + scores[3], scores[2] + scores[3]))

    else:
        pro1()


main()
