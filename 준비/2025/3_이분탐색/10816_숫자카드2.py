# 10816 -> 2792-> 3079 -> 2110 순서로 풀기
# 오늘은 2792 까지만 풀기

import sys


# 3_이분탐색 2회로 변경..
### 이분 탐색을 여러번 하는걸 주저하지 말기
### 해쉬테이블로 풀어도 된대. 난 용량 때문에 안하려 했는디 (dict 쓰면 나보다 조금 더 쓰긴 했는데, 그정돈 아니긴 함)
def solution2(N, deck, M, my_cards):
    deck.sort()  # O(500,000)
    anw_list = [0] * M
    for i in range(len(my_cards)):
        st_i = -1
        end_i = N
        while st_i + 1 < end_i:
            mid_i = (st_i + end_i) // 2
            # 나의 TG 값과 일치하는지 확인
            if deck[mid_i] < my_cards[i]:
                st_i = mid_i
            else:
                end_i = mid_i
        val_start_i = end_i
        # 없으면 한번 더 안해도 된다
        if end_i < N and my_cards[i] != deck[end_i]:
            continue

        # 같은게 몇개 있나 찾을 때도 이분탐색이 필요하다
        st_i = -1
        end_i = N
        while st_i + 1 < end_i:
            mid_i = (st_i + end_i) // 2
            # 나의 TG 값과 일치하는지 확인
            if deck[mid_i] <= my_cards[i]:
                st_i = mid_i
            else:
                end_i = mid_i
        val_end_i = st_i
        anw_list[i] = val_end_i - val_start_i + 1
    return anw_list


# deck 을 정렬하고 HashTable 로 바꾸면서, O(500,000) 정도를 좀 쓸 수는 없을까
# hashTable 사이즈가 너무 커서 안될 것으로 보임 500,000 이면 int 한쌍에 약 100~200 바이트.  Max 50만이면 50~100..
# 정렬 후 이분탐색으로 찾고, 경계지점을 찾아서, 몇 개까지인지 next 로 가면서 찾는다
# 들어있는 숫자  -10e6 ~ 10e6
def solution1(N, deck, M, my_cards):
    deck.sort()  # O(500,000)
    anw_list = [0] * M
    for i in range(len(my_cards)):
        st_i = -1
        end_i = N
        while st_i + 1 < end_i:
            mid_i = (st_i + end_i) // 2
            # 나의 TG 값과 일치하는지 확인
            if deck[mid_i] < my_cards[i]:
                st_i = mid_i
            else:
                end_i = mid_i
        # 크거나 같으면 end 를 줄이라 했으므로, 경계지점에서 end_i가 원하는 값
        # tg 값이랑 들어있는 값이랑 다르면 없는 것, 0표시, 맞으면 위로 몇 개 더 있는지 표시
        if end_i < N and deck[end_i] == my_cards[i]:  # 같으면 판단
            cnt = 0
            while end_i < N and deck[end_i] == my_cards[i]:
                cnt += 1
                end_i += 1
            anw_list[i] = cnt
    return anw_list


sys.stdin = open("input_10816.txt")
input = sys.stdin.readline

N = int(input())
deck = list(map(int, input().split()))
M = int(input())
my_cards = list(map(int, input().split()))
print(*solution2(N, deck, M, my_cards), end=" ")
