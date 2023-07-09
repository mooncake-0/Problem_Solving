import sys
from collections import deque

sys.stdin = open("input_2.txt")
input = sys.stdin.readline


def su(relationships):
    global rel_dict
    for x in relationships:
        if x[0] not in rel_dict:
            tmp = set()
            tmp.add(x[1])
            rel_dict[x[0]] = tmp
        else:
            rel_dict[x[0]].add(x[1])

        if x[1] not in rel_dict:
            tmp = set()
            tmp.add(x[0])
            rel_dict[x[1]] = tmp
        else:
            rel_dict[x[1]].add(x[0])


def solution(relationships, target, limit):  # limit 1 ~ 100
    global rel_dict, answer
    next_known = 0
    answer = 0
    rel_dict = dict()
    su(relationships)

    visited = set()
    visited.add(target)

    dq = deque()
    dq.append((target, 1))

    while dq:

        cur_node, times = dq.popleft()
        if times > limit:
            break
        for next_node in rel_dict[cur_node]:
            if next_node in visited:  # 안감
                continue
            visited.add(next_node)
            dq.append((next_node, times + 1))
            if times == 1:
                answer += 5
            else:
                answer += 10
                next_known += 1

    return answer + next_known


# rel < 4000
relationships = [[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]]
tg = 1
limit = 2
# 총 보상 + 새로 알게된 사람 수
print(solution(relationships, tg, limit))
