import sys

sys.stdin = open("input_3.txt")
input = sys.stdin.readline


def filter_special(string):
    for char in string:
        if char in special_with_space:
            string = string.replace(char, "")
    return string

def solution(merchantNames):
    global special_with_space

    merchantDict = dict()
    special_with_space = {"&", "(", ")", ".", ",", "-", " "}
    #보면서 제일 긴 점포를 확인해본다
    new_merchant = []
    for x in merchantNames:
        new_merchant.append(filter_special(x))

    for idx in range(len(new_merchant)):
        s = new_merchant[idx]
        if merchantDict:
            keys = list(merchantDict.keys()).copy()
            for key in keys:
                if s == key: # 대소 비교 필요
                    if len(merchantDict[key]) < len(merchantNames[idx]):
                        merchantDict[key] = merchantNames[idx]
                elif s in key: #
                    continue
                elif key in s: # 이 key 가 필요 없음
                    del merchantDict[key]
                    merchantDict[s] = merchantNames[idx]
                else: # 새 점포
                    merchantDict[s] = merchantNames[idx]

        else:
            merchantDict[s] = merchantNames[idx]

    # 한번 더 한다
    tmp = list(merchantDict.keys()).copy()
    del_keys = []
    for k_idx in range(len(tmp)):
        for k__idx in range(len(tmp)):
            if k_idx == k__idx:
                continue
            if tmp[k_idx] in tmp[k__idx]:
                del_keys.append(tmp[k_idx])
    for del_key in del_keys:
        del merchantDict[del_key]

    return list(merchantDict.values())



merchantNames = ["토스커피사일로 베이커리", "토스커피사일", "토스커피사일로 베이커", "토스커피사일로 베이", "토스커피사일로&베이커리"]
merchantNames2 = ["비바리퍼블리", "토스커피사일로 베이커리", "비바리퍼블리카 식당", "토스커피사", "토스커피사일로 베이커", "비바리퍼블리카식", "토스커피사일로 베이", "토스커피사일로&베이커리"]
print(solution(merchantNames2))