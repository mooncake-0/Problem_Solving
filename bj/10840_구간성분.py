import sys
from collections import Counter, defaultdict
 
sys.stdin = open('input.txt')   # 제출시에는 주석or제거
input = sys.stdin.readline
 
def getCnt(s):  # s = 길이 L 부분 문자열
    ''' List '''
    cnt = [0] * 26  # [a,b,..,z]
    for ch in s:
        #ord('a'): 97 ord('b'): 98  ord('A'): 65   ord('B'): 66
        cnt[ord(ch)-97]+=1
    return tuple(cnt)
 
    ''' Counter '''
    return Counter(s)
 
'''
Naive : O(N^4)
    L = min(len(A), len(B)) 부터 확인
    모든 쌍끼리 구간성분 확인
    길이 L 구간성분 확인 방법
     1) 정렬
        구하는비용 : O(L log L)
        비교하는비용: O(L)
     2) 빈도수
        구하는비용 : O(L)
        비교하는비용: O(26)
'''
def pro1():
    global L
    while L:
        for i in range(len(A)-L+1):     # A[i:i+L] 선택
            acnt = getCnt(A[i:i+L])     # O(L)
            for j in range(len(B)-L+1): # B[j:j+L] 선택
                bcnt = getCnt(B[j:j+L])
                if acnt == bcnt: return L
        L-=1
 
    return 0
 
'''
Hash 적용 : O(N^3)
길이 L인 A 구간 성분 저장
길이 L인 B 구간 성분 검색
'''
def pro2():
    global L
    while L:
        S = set()   # key = (a,b,c,d,e,...,z)
 
        ''' A의 길이 L인 모든 구간 성분 Hash에 등록 '''
        for i in range(len(A)-L+1):     # A[i:i+L] 선택
            S.add(getCnt(A[i:i+L]))     # O(L)
 
        ''' B의 길이 L인 모든 구간 성분 Hash에서 검색 '''
        for j in range(len(B)-L+1): # B[j:j+L] 선택
            if getCnt(B[j:j+L]) in S: return L
        L-=1
 
    return 0
 
'''
sliding window 기법 적용 : O(N^2)
길이가 정해진 부분수열(문자열)을 처리할 때 적용해볼 수 있음
ex) 길이 K인 부분 수열 합
    길이 K인 부문 문자열 문자 빈도수
'''
def pro3():
    global L
    while L:
        S = set()   # key = (a,b,c,d,e,...,z)
 
        ''' A의 길이 L인 모든 구간 성분 Hash에 등록 '''
        acnt = [0]*26
        for i in range(len(A)):
            acnt[ord(A[i])-97]+=1
            if i>=L: acnt[ord(A[i-L])-97]-=1
            if i>=L-1: S.add(tuple(acnt))
 
        ''' B의 길이 L인 모든 구간 성분 Hash에서 검색 '''
        bcnt = [0]*26
        for i in range(len(B)):
            bcnt[ord(B[i])-97]+=1
            if i>=L: bcnt[ord(B[i-L])-97]-=1
            if i>=L-1 and tuple(bcnt) in S:
                return L
 
        L-=1
 
    return 0
 
def main():
    global A, B, L
    A, B = input().strip(), input().strip()
    L = min(len(A), len(B))
    #print(pro1())
    #print(pro2())
    print(pro3())
main()