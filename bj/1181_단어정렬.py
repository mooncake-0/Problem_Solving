import sys

sys.stdin = open("input_1181.txt")

T = int(input())

for _ in range(T):

    n = int(input())
    
    list = []
    use_set = set()

    for _ in range(n):
        temp = input()
        use_set.add(temp)

    for i in use_set:

        list.append(i)

    list.sort(key=len)

    for i in list:
        print(i)
