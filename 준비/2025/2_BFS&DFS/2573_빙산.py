import sys

'''
recursion 한도를 높이니 메모리 초과 발생 했었다 -> python 이 예약해 놓는 Stack 용량이 높아서 그렇다고 함. 조절하니 통과함
> 참고로 메모리는 전보다 나은데, 시간은 약 2초 더 나왔음
> 이런 경우에는 메모리가 좀 여유롭기 때문에, 300 * 300 이면 행렬 하나 더 활용해도 됐었을 듯
> glacier 계산하는걸 마지막에 처리한다던가, 아니면 visited 를 for 룹 돌리지 않는다던가
>> 근데 두 요소가 시간에 지금 영향을 주는진 잘 모르겠다 솔직히.. glacier 계산도 for 문을 추가하는건 아니고, visited 도 for 문 두번 돌긴 하지만 위에 같은 Lv 의 for 문이 있어서 2*O(N^2) 정도고..
'''

sys.setrecursionlimit(10**5)  # 재귀 한도를 높임 (단, 무한루프 주의!)
input = sys.stdin.readline

# 할 일, DFS 수행, 수행하면서 주변에 맞춰서 얼음을 녹인다
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

I, J = map(int, input().split())
glaciers = [list(map(int, input().split())) for _ in range(I)]
visited = [[0] * J for _ in range(I)]
year_passed = 0


def dfs(position):
    minus_cnt = 0  # 주변에 바다가 몇개인고

    for i in range(4):
        mi = position[0] + di[i]
        mj = position[1] + dj[i]
        if 0 <= mi < I and 0 <= mj < J and glaciers[mi][mj] == 0 and visited[mi][mj] == 0: # 바다는 못가기 때문에 조건 추가
            minus_cnt += 1
        if 0 <= mi < I and 0 <= mj < J and glaciers[mi][mj] != 0 and visited[mi][mj] == 0:
            visited[mi][mj] = 1  # 탐색 찜
            dfs((mi, mj))

    # 종료될 때 녹이면서 종료
    glaciers[position[0]][position[1]] -= minus_cnt
    if glaciers[position[0]][position[1]] < 0:
        glaciers[position[0]][position[1]] = 0


while True:

    # 총 소요 년수
    chunk_cnt = 0  # chunk 가 없는 상황 catch
    chunk_divided = False

    # 올해 발생하는 모든 DFS 트리거 중 (visited 유지 필요)
    for i in range(I):
        for j in range(J):
            if glaciers[i][j] != 0 and visited[i][j] == 0:  # 얼음 부위이며, 올해 탐색한 적이 없다
                if chunk_cnt == 1:  # 1개 넘은 상황에서 cnt 가 추가된다
                    chunk_divided = True
                    break

                # DFS 트리거
                visited[i][j] = 1  # 판단 시작
                chunk_cnt += 1  # 분리된 chunk 는 일단 하나가 늘었음 (DFS 트리거 됐기 때문)
                dfs((i, j))

        if chunk_divided:  # 그만 돌려도 됨
            break

    # 탈출 상황 정의
    if chunk_divided or chunk_cnt == 0:
        if chunk_cnt == 0:
            year_passed = 0
        break

    # 탈출 안하는 상황이라면 year 을 증가시키고 visited 초기화 필요
    year_passed += 1
    for i in range(I):
        for j in range(J):
            visited[i][j] = 0

print(year_passed)
