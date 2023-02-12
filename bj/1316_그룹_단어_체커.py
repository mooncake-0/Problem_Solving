N = int(input())

checker = []
cnt = 0

for i in range(N):
    flag = True
    word = input()
    for j in range(0, len(word)):
        if word[j] in checker:
            if word[j - 1] is not word[j]:
                flag = False
                break
        else:
            checker.append(word[j])

    if flag:
        cnt += 1
    checker.clear()

print(cnt)
