import sys

sys.stdin = open("input_15686.txt")
input = sys.stdin.readline

'''
사고 흐름

>> 다해보려면 모든 치킨집 중 M 개를 고르는 조합을 구현해야함
>> 일단 치킨집 최대가 13개라는 점을 확인한 이후로는
>> 다해봐도 될것 같다는 생각
>> 대충 계산해보니 50 * 50 * MAX(2000) (이건 13C7값) * .. 해서 적어도 2억은 넘을 것 같음

>> 그러다 다시보니 빈 공간과 그래프는 아무 의미가 없다고 생각
>> 치킨집, 집 좌표계만 있으면, 바로 그 좌표계 내에서 for 문 돌리면 되니까 다 돌되, 50*50 이 사라져서 많이 줄어들음

>> 조합 방법으로 ㄱㄱ
>> 조합 (combination 구하기) 를 다시한번 구현해봄 (기본 DFS 문제) 

>> 각 LIST 를 돌면서, 최저들을 잘 판단해서 뽑아냈다. 
>> 다해봐야 할 것 같다고 무작정 다 ㄱㅈㅇ 하지 말고, 시간 복잡도를 생각해보고, 줄일 수 있는 방법이 있을까, 좌표만 따와서 작업할 수 있을까 등을 
   생각해보면 좋을듯

'''

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
house_list = []
chicken_list = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_list.append((i, j))
        if city[i][j] == 1:
            house_list.append((i, j))


def find_single_chicken_length(house_pos, chicken_pos):
    return abs(house_pos[0] - chicken_pos[0]) + abs(house_pos[1] - chicken_pos[1])


def find_all_chicken_length(using_chicken):
    # using_chicken 과 house_list 간에 all_chicken length 찾기
    anw = 0
    for k in range(len(house_list)):
        current_house_chicken_length = 50 * 50
        for l in range(len(using_chicken)):
            tmp = find_single_chicken_length(house_list[k], using_chicken[l])
            current_house_chicken_length = min(tmp, current_house_chicken_length)
        anw += current_house_chicken_length

    return anw


def dfs(c_idx, times, current):
    global total_anw
    if times >= M:
        # current 는 살아남은 치킨집들의 idx
        chck = find_all_chicken_length(current)
        total_anw = min(total_anw, chck)

    else:
        for i in range(c_idx, len(chicken_list)):
            current.append(chicken_list[i])
            dfs(i + 1, times + 1, current)
            current.pop()


def pro1():
    global total_anw
    total_anw = 10000000
    dfs(0, 0, [])
    print(total_anw)


def main():
    pro1()


main()
