# 갑자기 기본적인 조합 문제 풀어보기

def combination(n, start, used):
    if len(used) == n:
        print(used)
        all_combs.append(tuple(used))
        return
    else:
        for i in range(start, len(a)):
            used.append(a[i])
            # print("BEF", used)
            combination(n, i + 1, used)
            used.pop()
            # print("AF", used)


all_combs = []
a = ['a', 'b', 'c', 'd', 'e']
combination(3, 0, [])
print(all_combs)
