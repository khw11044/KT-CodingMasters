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

from itertools import combinations

if __name__=="__main__":
    A,B=map(int, input().split())
    print(len(list(combinations(range(1, A+1), B))))
    
    