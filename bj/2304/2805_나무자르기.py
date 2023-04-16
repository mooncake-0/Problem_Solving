import sys

sys.stdin = open("input_2805.txt")
input = sys.stdin.readline

# 상근이는 높이 H 를 지정
# 필요한 만큼만 가져가려 함
# 적어도 M 미터의 나무를 집에 가져가기 위해 설정할 높이의 최댓값
# 이정도 높이일 때 M 미터가 되니?

N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 나무의 높이는 항상 M 보다 크거나 같다
# 내가 설정할 높이
# 1로 설정하면 정말 많이 집에 가져가게 됨
# 내가 가장 높게는 가장 높은은 나무만큼 할 수 있다. -> 그럼 0m 긴 하겠지만
# 항상 답만이 범위에 들게 lt, rt 를 설정한다 >> lt < 모든 정답 < rt
lt = -1
rt = max(trees) +1 # O(1,000,000)


def checker(height):  # 이정도 높이일 때 가져갈 수 있는 나무가 M 이 되는가?
    count = 0
    for x in trees:
        if x > height:  # 내가 설정한 높이보다 x가 더 크면 잘린다# 내가 설정한 높이보다 작거나 같으면 아무것도 안잘린다
            count += x - height
    if count >= M:  # 자른 나무의 합이 만족하거나 넘쳐 난다. (height 를 늘려볼 수 있음)
        return True
    else:  # 부족하다. height 를 더 낮춰봐야 함
        return False


while lt + 1 < rt:  # lt+1 >= rt 일때까지 돈다
    mid = (lt + rt) // 2
    if checker(mid):  # height 늘리기
        lt = mid
    else:  # height 줄이기
        rt = mid

# 종료지점은 언제나 lt +1 = rt 인데, 언제나 경계지점이다
# 이 때는 생각을 하는 거임. 만족하고 있는데 늘려지고 싶은건가, 만족하는데 더 줄여보고 싶은건가.
# 더 늘려보고 싶은거면, lt 에서 만족해야 하는거고, 줄여보고 싶은거면 rt 에서 만족하는 것
print(lt)
