import sys

'''
s: 11:08
e: 11:30
- 연이은 combination 의 활용
'''

sys.stdin = open("input_14889.txt")
input = sys.stdin.readline

N = int(input())  # 찍수, 4~20
S = [list(map(int, input().split())) for _ in range(N)]


# index 0 ~ N-1 까지 중 N/2 개를 고르는 combination 계산
def combination(num, added):
    global start_teams_order
    if len(added) == N // 2:
        start_teams_order.append(added[:])
    else:
        for i in range(num, N):
            added.append(i)
            combination(i + 1, added)
            added.pop()


def comb2(num, added, team):
    global temp_sum
    if len(added) == 2:
        temp_sum += S[added[0]][added[1]]
        temp_sum += S[added[1]][added[0]]
    else:
        for i in range(num, len(team)):
            added.append(team[i])
            comb2(i + 1, added, team)
            added.pop()

def make_link_team(start_team):
    link_team = []
    for i in range(N):
        if i not in start_team:
            link_team.append(i)
    return link_team

def pro1():
    global start_teams_order, temp_sum
    start_teams_order = []
    combination(0, [])

    point_start_team = 10000000
    point_link_team = 0

    min_val = point_start_team - point_link_team

    # start team 이 아닌 애들은 link team
    for start_team in start_teams_order:

        link_team = make_link_team(start_team)
        temp_sum = 0
        comb2(0, [], start_team)
        point_start_team = temp_sum

        temp_sum = 0
        comb2(0, [], link_team)
        point_link_team =  temp_sum

        min_val = min(min_val, abs(point_start_team- point_link_team))

    print(min_val)

def main():
    pro1()


main()
