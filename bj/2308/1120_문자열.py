a, b = input().split()
str_counter = 51

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if b[j + i] != a[j]:
            count += 1
    if count < str_counter:
        str_counter = count

print(str_counter)