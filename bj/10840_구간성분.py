import sys

# sys.stdin = open("input_10840.txt")
input = sys.stdin.readline

'''
포인트
 - 정해진 대상에 대해선 고정 해싱을 생각해보는 것도 좋을 듯!
 - 꼭 문자열을 다 돌리지 않아도 파악할 수 있는 방법은 있음!
'''

def pro1(sa, sb):
    # print(sa, sb)
    the_saver = dict()  # 해당 튜플의 배열이 얼만큼 쓰였는지 저장해준다

    for box_size in range(1, len(sa) + 1):

        # print(box_size)
        # LIBRARY 초기화 필요
        library = dict()

        # 이정도는 매번 돌려줘도 됨
        for i in range(65, 91):
            tmp = chr(i)
            library[tmp.lower()] = 0

        for i in range(len(sa)):
            library[sa[i]] += 1
            if box_size - 1 <= i:  # 종료 시점을 잘 생각해야하는게, I 가 끝에 가야 끝임.
                #  지금 SA 를 잘라서 읽는게 아니라 INDEX 가 맨 뒤에서 나아가고 있기 때문에 종료조건이 그냥 끝임. 따라서 별도의 종료조건 필요 x
                if i >= box_size:  # 여기서부터는 빼기 시작해야 한다
                    # 빼는 로직 실행 , 자기가 하나씩 더 먹었으니, 뒤에 있는 애를 빼줘야 한다
                    library[sa[i - box_size]] -= 1
                the_saver[tuple(library.values())] = 0  # 그냥 사용된 이력이 있다 정도로 보관해 놓으면 된다

    # # 이젠 SB 를 파면서 위에 있는 tuple 과 비교하면 된다
    for box_size in range(1, len(sb) + 1):  # box_size 1 부터, 쭉 늘린다. box_size = sb 일 때까지

        library = dict()

        # 이정도는 매번 돌려줘도 됨
        for i in range(65, 91):
            tmp = chr(i)
            library[tmp.lower()] = 0

        # sb 도 똑같이 읽으면서, 사용되는 tuple 이력을 파볼 것이다.

        for i in range(len(sb)):
            library[sb[i]] += 1
            if i >= box_size - 1:  # box_size -1 부터는 저장되기 시작해야한다
                if i >= box_size:  # box_size 부터는 빼주기 시작해야 한다
                    library[sb[i - box_size]] -= 1
                # 이 시점에는 준비가 된 상태
                if tuple(library.values()) in the_saver:
                    the_saver[tuple(library.values())] += 1  # 이걸 확인해야 함
    # 다 준비되었음
    # the_saver 를 모두 돌면서 values 가 1 이상인 것 중에 제일 긴거 찾으면 끝
    max_length = 0
    for x in the_saver: # 모든 x 들에 대하여
        if the_saver[x] >= 1:
            max_length = max(max_length, sum(x))
    print(max_length)


def main():
    # for _ in range(int(input())):
    sa = input().strip()
    sb = input().strip()
    pro1(sa, sb)

    # for box_size in range(1, len(sa) + 1):  # 해당 box_size
    #     library = dict()
    #     for i in range(65, 91):  # dict 세팅
    #         library[chr(i)] = 0


main()
