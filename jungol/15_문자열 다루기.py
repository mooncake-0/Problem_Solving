'''
* init 호출 횟수 : 1회
> 모든 올바른 방향의 substring 과 모든 reverse 방향의 substring 까지 다 hash 에 저장하는
> global map 을 만들고 관리한다

* TC 별 pushBack() 호출 횟수 : 30,000 이하 max 4 글자

> x, y, xy 가 모든 기존 것에 다 붙게 되지만 그게 중요하기도 한듯?

* TC 별 popBack() 호출 횟수 : 100 이하

* TC 별 reverseStr() 호출 횟수 : 30,000 이하

* TC 별 getCount() 호출 횟수 : 30,000 이하

'''
'''
포인트
- 가장 오래걸릴 것 같은 함수들을 파악해서, 특정 자료구조로 부담을 분리하는 생각으로 시작
- 사실 String 을 다 살피면 time out 이라고 대놓고 말해줬기 때문에, 방법은 해싱으로 저장하면서 진행하는 방법 밖에 없음
- 함수별로 logging 을 달아놔서 어떤 지점에서 제일 오래걸리는지 확인할 수 있었다
- looping 시 수열식은 예시들로 그냥하면서 빠르게 하는게 좋아!
- Queue 를 적절히 잘 사용한 건 잘했음!
- 새로 알게된 포인트 : 
        -> (str).join(strB) --> O(len(strB))
        -> list([SEQUENCE 객체 (tuple, queue 등)]) --> O(len(SEQ객체)) 
        -> list[a:b] --> O(b-a) 
        -> list 에선 맨 앞에 insert 를 하면, 전체 다를 뒤로 당겨야 하기 때문에, O(N) 이 맞음
        -> 무심코 쓰는 것들의 Order 가 얼마나 높은지 확인할 수 있었다.
- Queue 는 인덱싱이 가능하다. 하지만 슬라이싱은 안된다. list 로 변환하고 슬라이싱 해야 하는데 그러면 list 화 및 slicing 까지 꽤나 부담 
'''


'''
TC별로 처음에 한번 호출된다.
초기문자열로 mainStr이 주어진다.
Parameters  mainStr : 초기 문자열 (소문자, 길이 1~30,000)
글로벌 map 을 만들어 놓고, 동작을 할 때마다 map 도 같이 관리해준다. 
# 마지막에서 전체 str 호출을 방지하기 위함
# 1번을 하고 바로 5번을 호출하는 예시를 보면, 전체 관할 map 이 무조건 하나 있어야 할 듯 해보임. 
# 그리고 reverse, pop, push 에 따라서 같이 관리해주는?

'''
from collections import deque


def init(mStr: str):
    global mainStr, reversedStr, isReversed, main_map, reversed_map
    mainStr = mStr
    reversedStr = mStr[::-1]
    # 현재 상태를 본다
    isReversed = False
    # main map 과, reversed map 을 init 에서 준비한다
    main_map = dict()
    reversed_map = dict()

    for box_size in range(1, 5):  # box_size 는 1~4
        for i in range(len(mainStr) - box_size + 1):  # abcdef 면, 012345
            # 각각에 대해 저장한다
            tmpStr = mainStr[i: i + box_size]
            if tmpStr in main_map:
                main_map[tmpStr] += 1
            else:
                main_map[tmpStr] = 1

    for box_size in range(1, 5):
        for i in range(len(reversedStr) - box_size + 1):  # abcdef 면, 012345
            # 각각에 대해 저장한다
            tmpStr = reversedStr[i: i + box_size]
            if tmpStr in reversed_map:
                reversed_map[tmpStr] += 1
            else:
                reversed_map[tmpStr] = 1

    mainStr = deque(mStr)
    reversedStr = deque(reversedStr)


'''
void pushBack(char newStr[])
mainStr 맨 뒤에 newStr 문자열을 추가한다.
Parameters   newStr : 끝에 붙일 문자열 (소문자, 길이 1~4)
'''


def buildQueToStr(deq, s, e):
    str = ''
    for i in range(s, e):
        str += deq[i]
    return str


def pushBack(mWord: str):
    global mainStr, reversedStr, isReversed, main_map, reversed_map
    for x in mWord:
        if not isReversed:  # 정상 상태면 정상으로 넣고, reversedStr 에는 거꾸로 넣는다
            mainStr.append(x)
            reversedStr.appendleft(x)
        else:
            mainStr.appendleft(x)
            reversedStr.append(x)

    if not isReversed:  # 정상 상태
        for box_size in range(1, 5):  # main_map 에는 정상대로 추가한다
            for k in range(len(mainStr) - len(mWord) - box_size + 1, len(mainStr) - box_size + 1):
                if k >= 0:  # 음수인 경우면 판단 안해도 됨
                    # 지금 같은 경우면, t, k, ot, tk , otk 이렇게 추가되는걸텐데
                    # 이거 그대로 반대로 하면 t, k, to, kt, kto 가되는데 이거 그대로 아래 map 에 추가해주면 되는듯?
                    tmp = buildQueToStr(mainStr, k, k + box_size)
                    # tmp = ''.join(list(mainStr)[k:k + box_size])
                    if tmp in main_map:
                        main_map[tmp] += 1
                    else:
                        main_map[tmp] = 1

                    tmp_rev = tmp[::-1]

                    if tmp_rev in reversed_map:
                        reversed_map[tmp_rev] += 1
                    else:
                        reversed_map[tmp_rev] = 1
    else:
        for box_size in range(1, 5):  # main_map 에는 정상대로 추가한다
            for k in range(len(reversedStr) - len(mWord) - box_size + 1, len(reversedStr) - box_size + 1):
                if k >= 0:  # 음수인 경우면 판단 안해도 됨
                    # 지금 같은 경우면, t, k, ot, tk , otk 이렇게 추가되는걸텐데
                    # 이거 그대로 반대로 하면 t, k, to, kt, kto 가되는데 이거 그대로 아래 map 에 추가해주면 되는듯?
                    tmp = buildQueToStr(reversedStr, k, k + box_size)
                    # tmp = ''.join(list(reversedStr)[k:k + box_size])
                    if tmp in reversed_map:
                        reversed_map[tmp] += 1
                    else:
                        reversed_map[tmp] = 1

                    tmp_rev = tmp[::-1]

                    if tmp_rev in main_map:
                        main_map[tmp_rev] += 1
                    else:
                        main_map[tmp_rev] = 1


'''
void popBack(int n)
mainStr의 맨 뒤에 n개의 문자를 제거한다.
n은 호출 시점의 mainStr의 길이보다 작음이 보장된다.
Parameters n : 제거할 문자의 개수 (1 ≤ n < 문자열 길이)
'''


# 100 이하로 호출
# 이건 사실 새로운 dict 을 만들어주는게 더 빠를 듯
# JOIN = O(N)  // SLICING O(B-A) // STRLENGTH = 30000 // ITER 5
# 다하면 1억 넘음 ..
def popBack(k: int):
    global mainStr, reversedStr, isReversed, main_map, reversed_map
    # 빼기 전에.... 빠질 애들에 대해서 파악해볼 것임
    if not isReversed:  # 정상 상태에서는 기본에서는 뒤에서 뺄 것이고,
        for box_size in range(1, 5):
            for t in range(len(mainStr) - k - box_size + 1, len(mainStr) - box_size + 1):
                if t >= 0:  # 음수인 경우면 판단 안해도 됨
                    # 지금 같은 경우면, t, k, ot, tk , otk 이렇게 추가되는걸텐데
                    # 이거 그대로 반대로 하면 t, k, to, kt, kto 가되는데 이거 그대로 아래 map 에 추가해주면 되는듯?
                    tmp = buildQueToStr(mainStr, t, t + box_size)
                    # tmp = ''.join(list(mainStr)[t:t + box_size])
                    main_map[tmp] -= 1  # 당연히 있을 것이고, 해당을 -1 한다

                    tmp_rev = tmp[::-1]
                    reversed_map[tmp_rev] -= 1  # 반대쪽에도 당연히 있을 것이고, -1 한다

    else:
        for box_size in range(1, 5):  # main_map 에는 정상대로 추가한다
            for t in range(len(reversedStr) - k - box_size + 1, len(reversedStr) - box_size + 1):
                if t >= 0:  # 음수인 경우면 판단 안해도 됨
                    # 지금 같은 경우면, t, k, ot, tk , otk 이렇게 추가되는걸텐데
                    # 이거 그대로 반대로 하면 t, k, to, kt, kto 가되는데 이거 그대로 아래 map 에 추가해주면 되는듯?
                    tmp = buildQueToStr(reversedStr, t, t + box_size)
                    # tmp = ''.join(list(reversedStr)[t:t + box_size])
                    reversed_map[tmp] -= 1

                    tmp_rev = tmp[::-1]
                    main_map[tmp_rev] -= 1

    # map 은 처리 되었고, 이제 찐 원소에서 뺀다
    for i in range(k):
        if not isReversed:  # 정상이면 mainStr 정상 빼기, reversedStr 앞에서 빼기
            mainStr.pop()
            reversedStr.popleft()
        else:  # 뒤집은 상태면 reversed 를 정상 빼기
            mainStr.popleft()
            reversedStr.pop()


'''
    for box_size in range(1, 5):
        for i in range(len(mainStr) - box_size + 1):
            tmp = ''.join(list(mainStr)[i:i + box_size])
            if tmp in main_map:
                main_map[tmp] += 1
            else:
                main_map[tmp] = 1

            tmp2 = ''.join(list(reversedStr)[i:i + box_size])
            if tmp2 in reversed_map:
                reversed_map[tmp2] += 1
            else:
                reversed_map[tmp2] = 1
'''


'''
mainStr을 뒤집는다.
'''


# 좀 의심스럽. 30000 번 호출
def reverseStr():
    global isReversed
    # global tgStr
    # tgStr = tgStr[::-1]
    if isReversed:
        isReversed = False
    else:
        isReversed = True


'''
mainStr에서 subStr이 등장하는 횟수를 반환한다.
문자열이 겹치는 경우도 중복해서 센다.
예를들어 "aaa" 에서 "aa"의 등장 횟수는 2회이다.
mainStr을 전체 탐색하면 시간 초과가 발생할 수 있다.
Parameters
  subStr : 등장 횟수를 세기위한 문자열 (소문자, 길이 1 ~ 4)
Returns
  mainStr에서 subStr의 등장횟수 반환
  '''


# NAIVE 구현 -> 30,000 개의 str, 30,000번 호출
# >> 900,000,000 9억..
def pro1(mWord) -> int:
    global tgStr
    box_size = len(mWord)
    cnt = 0
    for i in range(len(tgStr) - box_size + 1):
        # SLICING 시간복잡도도 있음. O(b-a 정도) 만큼이라고 함.
        if mWord == tgStr[i:i + box_size]:
            cnt += 1
    return cnt


def getCount(mWord: str) -> int:
    # 다른건 맞는지 파악하기 위해 NAIVE 하게 우선 구현해보자
    # return pro1(mWord)
    # return pro2(mWord)
    global mainStr, reversedStr, isReversed, main_map, reversed_map
    if isReversed:  # 뒤집혀진 상태면 reversed_map 에서 찾는다
        if mWord in reversed_map:
            return reversed_map[mWord]
    else:
        if mWord in main_map:
            return main_map[mWord]
    return 0

