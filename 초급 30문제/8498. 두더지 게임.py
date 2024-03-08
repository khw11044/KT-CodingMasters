'''
월미도 게임랜드에는 두더지 게임 기계가 있습니다. 
기계는 8 X 8 칸의 판으로 이루어져 있고, 모양은 이러합니다.

0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0

두더지는 0에 해당하는 위치에서만 올라올 수 있습니다. 
1에 해당하는 칸에서는 두더지가 존재한다 해도 구멍이 막혀있어 올라올 수 없습니다. 

기계 아래 어느 칸에 두더지가 있는지에 대한 정보가 주어질 때, 
두더지가 올라올 수 있는 칸의 개수를 알아내는 프로그램을 작성하세요.
-------------------------------------------
[입력값 설명]
총 8개의 줄에 걸쳐서 길이가 8이고 알파벳 대문자 T와 F로만 이루어진 문자열이 주어집니다.
i번째 줄의 j번째 글자는 i번째 줄 j번째 칸의 기계 아래의 상태를 의미합니다.

[출력값 설명]
두더지가 올라올 수 있는 칸의 개수를 출력합니다.
--------------------------------------------------

예제 입력1
TFFTTFTT
FTFTFTTF
TTTFTFTT
TTTTFFTT
TFTTFTFT
TTTFFTTF
TFTFTFTT
TFTFTTFT

예제 출력1
9

예제 입력2
TFFTTFTT
FTFTFTTF
TTTFFTTF
TFTFTFTT
TFTFTTFT
TTTFFTTF
TFFTTFTT
FTFTFTTF

예제 출력2
11
'''
# 

import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline


if __name__=="__main__":
    N=8
    hols = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]
    ] 
    board = [list(input().rstrip()) for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if hols[i][j]==0 and board[i][j]=='F':
                cnt+=1
    print(cnt)
    
    