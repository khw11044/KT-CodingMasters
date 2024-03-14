'''
정수 A와 B가 입력될 때 ,
A개의 원소에서 B개의 원소를 뽑는 조합에 대한 총 경우의 수를 출력하는 프로그램을 작성하세요.
-------------------------------------------
[입력값 설명]
첫 번째 줄에 정수 A와 B가 공백을 기준으로 입력됩니다. (1 ≤ B ≤ A ≤ 30)

[출력값 설명]
A개의 원소에서 B개의 원소를 뽑는 조합에 대한 총 경우의 수를 출력합니다.
--------------------------------------------------

예제 입력1
10 5

예제 출력1
252

예제 입력2
7 2

예제 출력2
21
'''
# 


import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline

# 조합 : nCr = n! // (n-r)! * r!
def comb(n, r):
    a = 1 
    b = 1
    if n == r or r==0:
        return 1
    for i in range(r):
        a *= (n-i)  # n!/(n-r)! -> 즉, n*(n-1)*(n-2)* ... *(n-r)
        b *= (r-i)  # r!
    return a//b

if __name__=="__main__":
    A,B=map(int, input().split())   # A개의 원소들에서 B개를 뽑기
    print(comb(A, B))


'''
DP로 푸는 법 
import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline

if __name__=="__main__":
    A,B=map(int, input().split())   # A개의 원소들에서 B개를 뽑기
    dp = [[0]*(B+1) for _ in range(A+1)]

    for a in range(A+1):
        for j in range(min(a, B) + 1):
            if j == 0 or j == a:
                dp[a][j] = 1
            else:
                dp[a][j] = dp[a-1][j-1] + dp[a-1][j]
    
    print(dp[A][B])
'''

'''
# from math import comb 로 푸는 법 
import sys
input=sys.stdin.readline

from math import comb

# 입력 받기
A, B = map(int, input().split())

# A개의 원소에서 B개의 원소를 뽑는 조합의 경우의 수 계산
result = comb(A, B)

# 결과 출력
print(result)

'''
