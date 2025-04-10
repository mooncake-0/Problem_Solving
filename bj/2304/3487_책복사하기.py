import sys

sys.stdin = open("input_3487.txt")
input = sys.stdin.readline

'''
포인트

    -1 판별할 수 없는 건 판별할 수 없는 것. 다른 방법 찾아야 함 -> 이 녀석이 다른 조합이 있는? 있을 수 있지만 모두 판단하는건 불가능
    -2 마지막에 숫자 판단을 어디서 해주냐가 굉장히 미묘했음
    -3 근데 사실 2613 번에서 해당 부분은 다 해놔서, 사실 Detail 한 print 에서 차이났던 부분인 듯
    -4 m, k 를 그냥 줄여가면서 판단하면 훨씬 쉬웠을 듯
    -5 답을 구해놓고, 마지막에 한바퀴 더돌면서 판단시키는게 더 깔끔한 코딩 --> 2613 도 그렇게 되어도 될듯
       --> 이렇게 되면 check 함수가 간단해지거든 (막 마지막거만 돌리려고 doCheck 이딴 짓 하는거보단 .. )
       
'''


# 최대 페이지가 이정도 된다면 서기공 k 명으로 되는가?
# 각 서기공이 담당하는 페이지 수까지 같이 출력 필요
def check(limit):
    # global each_pages_index
    # 한 페이지씩 추가해가면서 limit 을 넘게 되면 서기공 들어온다
    scribers = 0
    sum = 0
    # tmp_l = []
    for i in range(len(book_pages)):
        tmp = sum + book_pages[i]  # 이번 것을 더한다면
        if tmp > limit:  # 더했을 때 더 커진다
            scribers += 1
            sum = book_pages[i]
            # if doCheck:
            #     each_pages_index.append(tmp_l)
            # tmp_l = [i]
            # 이 때, 남은 책 수와 남은 구독자 수가 동일하다면 1:1  매칭해야한다
            # 이 조건에 들어올 수 있다는거 자체가 일단 합격임
            # if doCheck:
            #     if len(book_pages) - i == k - scribers:
            #         for j in range(i, len(book_pages)):
            #             each_pages_index.append([j])
            #         return True
        else:  # 그냥 더하면 된다
            sum += book_pages[i]
            # tmp_l.append(i)
    # 마지막 묶음을 위해 더해준다
    scribers += 1
    # if doCheck:
    #     each_pages_index.append(tmp_l)
    # 모두 종료시, scribers 수를 판단한다
    if scribers > k:  # scribers 가 너무 많이 필요. limit 을 넓혀야 함
        return False
    else:  # scribers 여유 있거나 매치 함. limit 을 줄여볼 필요
        return True


def pro1():
    global m, k, book_pages  # 이 sequence 대로 작업
    # 비슷한듯. 가장 많은 책을 담당하는 서기공의 페이지 수의 최소
    # 가장 많은 페이지 한권
    lt = max(book_pages) - 1  # 범위 안에 들여놓기 위함
    rt = sum(book_pages) + 1  # 한 명이 전부 담당]
    # 기본적인 3_이분탐색 Set
    while lt + 1 < rt:
        mid = (lt + rt) // 2
        if check(mid):  # 줄여보자
            rt = mid
        else:
            lt = mid
    # 끝나고 나면 lt +1 = rt 경계면
    # lt 는 부족해서 늘리는 중 ( 안되는 수) / rt 는 줄여보는 중 (되는 수)
    # 정답은 rt 이므로, 최종 list check 을 위해 한번 더 진행한다
    # 일은 최대한 뒤쪽이 해줘야 함
    # POINT - 채워 넣는 과정이 MAX 를 넣어야 편하므로, 뒤집고 마지막에도 뒤집는다

    li = []
    gsum = 0
    for x in book_pages[::-1]:
        gsum += x # 이번 책을 더할경우 일어나는 일을 생각해본다

        # 책의 수가 서기공보다 많아야 이 로직이 돌아가는건데,
        # 딱 같을 때까진
        # 책의 수가 서기공보다 적어지기 시작
        if gsum > rt or m < k:  # 먼저 gsum 이 초과될 거고
            li.append("/")  # 구분을 해줄 거다
            gsum = x  # 현재걸로
            k -= 1  # 서기공을 줄인다

        li.append(x)  # 어쨌든 현재 것을 appending 을 한다
        m -= 1  # 이 책은 썼으니 버린다

    print(*li[::-1])


# 대본 m 권, 서기공 k
# 한 권 이상씩의 대본 배
def main():
    global m, k, book_pages
    for _ in range(int(input())):
        m, k = map(int, input().split())
        book_pages = list(map(int, input().split()))
        pro1()


main()
