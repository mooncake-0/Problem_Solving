import sys

pok_dict = dict()
num_dict = dict()
n, m = map(int, input().split())

for idx in range(1, n+1):
    pok = input().strip()
    num_dict[idx] = pok
    pok_dict[pok] = idx

for _ in range(m):
    a = input().strip()
    if a in pok_dict:
        print(pok_dict[a])
    else:
        a = int(a)
        print(num_dict[a])
