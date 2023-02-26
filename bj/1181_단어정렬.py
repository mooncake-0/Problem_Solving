import sys

sys.stdin = open("input_1181.txt")

T = int(input())

for _ in range(T):
    n = int(input())
    array = []
    setArray = set()
    for _ in range(n):
        alphabet = input()
        setArray.add(alphabet)

    for i in setArray:
        array.append(i)

    array.sort()
    array.sort(key=len)

    for i in array:
        print(i)
