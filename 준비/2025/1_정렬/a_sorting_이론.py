## 버블 정렬
## 인접한 두 수를 비교해서 작은 값을 지속적으로 앞으로 보낸다
## 시간복잡도 O(N^2) - 단순한 만큼 비효율적
def bubble_sort(_arr):
    for i in range(len(_arr)):  # 1번 실행에서, 2번 실행에서, ...
        for j in range(len(_arr) - 1 - i):  # 맨 뒤에 가장 큰 수가 쌓이므로, 하나씩 덜해가도 됨 (-0,-1,-2, .. 보니까 -i 더라)
            if _arr[j] > _arr[j + 1]:
                _arr[j], _arr[j + 1] = _arr[j + 1], _arr[j]
    return _arr


## 선택 정렬
## 매번 가장 작은 것을 선택해서 앞에 있는 데이터와 바꾸는 과정 (원시적)
## 2중 반복문 사용으로 O(N^2) 의 복잡도 - 매우 비효율적
## 그래도 데이터가 10000개 이하면 쓸만하다고 한다
## 매우 기초 정렬의 모습. 익숙해지면 좋다
def selection_sort(_arr):
    for i in range(len(_arr)):
        min_index = i  # 시작이 제일 작다고 생각
        for j in range((i), len(_arr)):
            if _arr[min_index] > _arr[j]:
                min_index = j
        _arr[i], _arr[min_index] = _arr[min_index], _arr[i]
    return _arr


## 퀵정렬
## 빠르고, 정렬라이브러리들의 근간이 된다
## pivot 등장 - 큰 수와 작은 수에 대한 "기준"
## 평균 시간 복잡도 O(NlogN) (하지만 최악은 O(N^2) 이라고 함) -> 항상 최솟값/최댓값이 피벗으로 선택되면 최악 (그만큼 더 loop 를 많이 돌려야 하기 때문) - 피벗 선택을 좀 더 랜덤값? 머 이런걸로 하면 낫다고 함
def quick_sort(_arr):
    if len(_arr) <= 1:
        return _arr
    pivot = _arr[len(_arr) - 1]
    left_arr = []
    right_arr = []
    for i in range(len(_arr)):
        if i == len(_arr) - 1:
            continue
        if pivot >= _arr[i]:
            left_arr.append(_arr[i])
        else:
            right_arr.append(_arr[i])

    '''
    GPT 조언 - list comprehension 사용
    pivot = _arr[-1]  # 마지막 요소를 피벗으로 선택
    ## 참고로 x in _arr[:-1] 인 이유는 항상 마지막 요소는 제외해야 하기 때문!! (pivot 값은 따로 더해지기 때문)
    left_arr = [x for x in _arr[:-1] if x <= pivot]  # 피벗보다 작은 값
    right_arr = [x for x in _arr[:-1] if x > pivot]  # 피벗보다 큰 값
    '''
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


## 병합정렬 - O(NlogN) - 공간은 넉넉하고 시간 복잡도가 반드시 보장되어야 할 때
## 대량 데이터에 적합. 하지만 추가적인 메모리 공간이 필요함 (공간 복잡도 O(N))
def merge_chunk(arr1, arr2):
    # 둘 중 하나가 끝에 도달할 때 까지 돌린다
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # 남은 것들을 더해준다 (arr1, arr2 는 항상 정렬된 상태이므로 남은걸 그냥 더해줘도 정렬되어 있다)
    if i == len(arr1):
        merged += arr2[j:]
    elif j == len(arr2):
        merged += arr1[i:]
    return merged


def merge_sort(_arr):
    # 결국 잘린거 두 개를 merge 함
    if len(_arr) == 1:
        return _arr
    mid = len(_arr) // 2
    l_arr = _arr[:mid]
    r_arr = _arr[mid:]
    return merge_chunk(merge_sort(l_arr), merge_sort(r_arr))


given_arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# print(bubble_sort(given_arr))
print(selection_sort(given_arr))
# print(quick_sort(given_arr))
# print(merge_sort(given_arr))
