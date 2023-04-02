import sys

sys.stdin = open("input_midas.txt")
input = sys.stdin.readline

option_list = ["W"]

#OPTION 이 F 일 경우에는 history 들 중 문자를 기준으로 검색한다
#T 일 경우에는 각 단어별로 검색한다
# W 같은 경우는 keyword 와의 일치 여부를 판단한다
# 입력이 없을경우 기본적으로 F로 동작
def solution(history, option, keyword):

    anw = []
    if option:
        if "T" in option[0]:
            for k in history:
                tmp = k.split(" ")
                if keyword in tmp:
                    anw.append(k)
        else:
            for k in history:
                if keyword == k:
                    anw.append(k)
    return anw

history = ["hello i am david","hello kail","hi tina"]
option =[["W","T"]]
keyword = "hell"

print(solution(history,option, keyword))

'''

def main():
    global history, options
    raw_hist = input().strip()
    raw_hist = raw_hist[1:len(raw_hist)-1]
    tmp = raw_hist.split(",")
    history = []
    for x in tmp:
        x = x[1:len(x)-1]
        history.append(x)

    raw_option= input().strip()
    raw_option= raw_option[2:len(raw_option)-2]
    tmp = raw_option.split("],[")
    options =[]
    for x in tmp:
        k = x.split(",")
        single = []
        for t in k:
            single.append(t[1:len(t)-1])
        options.append(single)

    keyword = input().strip()
    keyword = keyword[1:len(keyword)-1]

    return find_suggestions(keyword)

main()
'''

'''
input
['history1', 'history2',...'historyN']


'''