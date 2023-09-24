n = int(input())
anw = 0

for i in range(1, n + 1):
    if i < 100:
        anw += 1
    if i >= 100:
        temp1 = int(str(i)[0]) - int(str(i)[1])
        temp2 = int(str(i)[1]) - int(str(i)[2])
        if temp1 == temp2:
            anw += 1

print(anw)
