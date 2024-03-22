'''
농부 민겸은 밭에서 농사를 짓습니다.

민겸의 밭은 N × N 크기의 정사각형 모양입니다. 
즉, N^2개의 1 × 1 크기의 땅으로 나눌 수 있습니다. 

각 땅은 빈 땅, 작물만 있는 땅, 잡초만 있는 땅으로 구분됩니다. 

민겸은 잡초를 손쉽게 제거하기 위해 최첨단 오리 농법을 도입했습니다.

오리 인덕이는 식탐이 많기 때문에 민겸이 정한 어떤 가로줄 또는 세로줄의 잡초와 작물을 모두 먹습니다. 
인덕이가 먹을 수 있는 양에 한계는 없고, 민겸은 인덕이를 원하는 만큼 이용할 수 있습니다.

똑똑한 민겸은 인덕이를 적절히 이용하여 모든 작물을 보존하면서 최대한 많은 잡초를 없앴습니다.
이때 잡초만 있는 땅이 몇 개 남아있는지 알려주는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『입력은 여러 개의 줄로 주어집니다.

첫 번째 줄에는 밭의 가로와 세로의 길이 N이 주어집니다. (1 ≤ N ≤ 5)

두 번째 줄부터 N개의 줄에는 밭의 정보가 공백으로 구분되어 주어집니다.
0은 빈 땅, 1은 작물만 있는 땅, 2는 잡초만 있는 땅입니다.』

[출력값 설명]
『남아있는 잡초만 있는 땅이 몇 개인지 출력합니다.』
------------------------------------------------------------------------
예제 입력1
4
1 0 1 0
0 2 0 2
2 0 0 0
2 1 2 2

예제 출력1
2

예제 입력2
4
0 0 1 2
1 2 0 2
0 0 0 1
2 1 0 0

예제 출력2
4
'''


# 문제의 핵심은 모든 작물을 보존하면서 최대한 많은 잡초를 제거하는것 
# -*- coding: utf-8 -*-
import sys 
sys.stdin=open('input.txt', 'r')
input = sys.stdin.readline

if __name__=="__main__":
    N=int(input())
    garden = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        if 1 not in garden[i]:
            garden[i] = [0]*N
    
    garden = list(zip(*garden))
    
    for i in range(N):
        if 1 not in garden[i]:
            garden[i] = [0]*N
            
    res = 0
    for i in range(N):
        res += garden[i].count(2)
    
    print(res)
