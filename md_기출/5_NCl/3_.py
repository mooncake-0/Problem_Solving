import sys


sys.stdin = open("input_3.txt")
input = sys.stdin.readline
# 효율적인 알고
# 갯수는 2 ~ 10만개
# K 는 1 ~ 10만 (길이)
# 전체 비교 말고는 근데 답이 없다
#
def is_valid(candidate, words):
    """ 주어진 candidate 문자열이 words의 모든 문자열과
        최대 한 글자만 다른지 확인하는 함수 """
    for word in words:
        diff = sum(c1 != c2 for c1, c2 in zip(candidate, word))
        if diff > 1:
            return False
    return True

def solution(words):
    base = words[0]  # 기준이 될 첫 번째 단어
    K = len(base)  # 단어의 길이 (모든 단어는 동일한 길이)

    # 각 자리에서 가능한 모든 문자를 시도하며 candidate를 생성
    for i in range(K):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            candidate = base[:i] + ch + base[i+1:]
            if is_valid(candidate, words):
                return candidate  # 조건을 만족하는 후보 문자열을 찾으면 반환

    return ""  # 조건을 만족하는 문자열이 없으면 빈 문자열을 반환


TC = int(input())
for _ in range(TC):
    a = list(map(str, input().split()))
    print(a)
    print(solution(a))
