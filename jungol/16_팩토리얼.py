import sys

input = sys.stdin.readline

def recursion(num):
    if num == 1:
        print("1! = 1")
        return 1
    print(str(num) + "! = " + str(num) + " * " + str(num-1) + "!")
    return recursion(num-1)*num


def main():
    a = int(input())
    print(recursion(a))


main()