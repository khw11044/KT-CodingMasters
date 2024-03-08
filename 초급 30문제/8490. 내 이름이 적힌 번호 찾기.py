'''
N개의 서로 다른 정수가 정렬된 상태로 입력이 될 때,
특정한 원소 A가 몇 번째에 위치해 있는지 알려주는 프로그램을 작성하세요. 

단, 특정한 원소 A를 찾을 수 없을 때는 -1을 출력합니다.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 정수의 개수 N과 특정한 원소 A가 공백으로 구분되어 입력됩니다.
(1 ≤ N ≤ 1,000,000, 1≤ A ≤ 10,000,000)

이후에 N개의 서로다른 정수 K가 공백을 기준으로 입력됩니다. (1 ≤ K ≤ 10,000,000)』

[출력값 설명]
『특정한 원소 A가 몇 번째에 위치해 있는지 출력합니다.
단 특정한 원소 A를 찾을 수 없을 때는 -1을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
5 BENJAMIN
GENNADY LINGYU ALEX BENJAMIN MIFAFA

예제 출력1
4

예제 입력2
10 G
A B C D E F G H I J

예제 출력2
7
'''

# -*- coding: utf-8 -*-
import sys
sys.stdin=open('input.txt', 'r')
input = sys.stdin.readline

if __name__=="__main__":
    # 입력 받기
    N, name = map(str, input().split())
    N = int(N)
    name_list = list(map(str, input().split()))
    for i,n in enumerate(name_list,1):
        if n == name:
            print(i)
    
    
                 
                 