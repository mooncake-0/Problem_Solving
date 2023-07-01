scenario = 0
while True:
    n = int(input())
    if n == 0:
        break
    scenario += 1
    student = [input() for _ in range(n)]
    earring = {}
    for i in range(2 * n - 1):
        num, alphabet = input().split()
        if num in earring:
            del earring[num]
        else:
            earring[num] = alphabet
    angry = int(next(iter(earring)))
    print(scenario, student[angry - 1])