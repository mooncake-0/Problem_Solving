import sys

'''
s 10:08
e 10:48
- 스택을 써야 한다는 생각을 갖는것도 살짝 어려울 듯. PQ 생각이 가장 먼저 들긴 함
- 스택을 썼을 때도 어떻게 해야하는지도 난 살짝 어려웠음 - 개인적으로 G4 정도로 생각
- 다양하게 사용, 두개를 사용 등등
'''

sys.stdin = open("input_2493.txt")
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
anws = [0] * N


def pro2():
    tmp = []
    popped_idx = N - 1
    while towers:
        hi = towers.pop()
        if tmp:
            if tmp[len(tmp) - 1][0] > hi:  # 그냥 저장하고 끝내야 함
                tmp.append((hi, popped_idx))
            else:  # 더 작음
                while tmp and tmp[len(tmp) - 1][0] < hi:
                    numb, cidx = tmp.pop()
                    anws[cidx] = popped_idx + 1
                tmp.append((hi, popped_idx))

        else:
            tmp.append((hi, popped_idx))

        popped_idx -= 1

    # 남은 애들은 모두 0 이다
    while tmp:
        numb, cidx = tmp.pop()
        anws[cidx] = 0

    print(*anws)


''' 500,000 * 500,000 .. 당연히 time out / 0에 대한 탐색을 줄이는 방안 or 아예 다른 접근 필요'''
def pro1():
    while towers:
        tgIdx = len(towers) - 1
        tg = towers.pop()
        for idx in range(len(towers) - 1, -1, -1):
            if towers[idx] > tg:
                anws[tgIdx] = idx + 1
                break
    print(*anws)


def main():
    # pro1()
    pro2()


main()
