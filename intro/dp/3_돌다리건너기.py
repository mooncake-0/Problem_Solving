import sys

N = int(input())

# 3<= n <= 45
# 한 칸 혹은 두 칸
# ㅇ _ ____  1 + 1 // 2  f(1) = 2
# ㅇ _ _ ____ // (1+1+1)  // (2+1) // (1+2) f(2) =3
# o _ _ _ ____ // (1+1+1+1) // (2+1+1) // (1+2+1) // 1+1+2 // (2+2)  f(3) = f(1) + f(2)

def main():
    pro = [0] * (N + 1)
    pro[1] = 2
    pro[2] = 3
    for i in range(3, len(pro)):
        pro[i] = pro[i-1] + pro[i-2]
    print(pro[N])

main()
