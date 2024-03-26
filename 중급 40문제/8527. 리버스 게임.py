'''
리버스라는 보드 게임이 있습니다.
게임 규칙은 이러합니다.
두 명이서 가위바위보를 하고, 
이긴 사람은 바둑판에 앞면은 검은색, 뒷면은 흰색인 바둑들을 임의로 깔아놓습니다.

가위바위보에서 진 사람은 바둑돌을 뒤집을 수 있는데, 
한번 뒤집을 때 해당 열이나 행의 모든 바둑돌을 뒤집어야 합니다. 

예를 들어 3 X 3 형태로 바둑돌이 놓여져 있을 때 원하는 바둑돌 하나만 뒤집을 수는 없고,
특정한 열이나 행에 해당하는 바둑돌 3개를 모두 뒤집어야 합니다.
게임에서 이기기 위해서는 원하는 만큼 바둑돌을 뒤집어서 위에서 보이는 흰색 바둑돌의 개수가 최소가 되어야 합니다.

자연수 N이 주어지고, N X N 형태의 바둑돌들이 주어질 때 
바둑돌을 뒤집는 사람이 만들 수 있는 위에서 보이는 흰색 바둑돌의 최소 개수를 출력하는 프로그램을 만드세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 자연수 N이 주어집니다. (1 ≤ N ≤ 10)

둘째 줄부터 N개의 줄에 걸쳐 바둑돌들의 상태가 길이가 N인 문자열로 주어집니다.

i번째 문자열의 j번째 문자가
'B'인 경우 i행 j열의 바둑돌의 윗면이 검은색이고,
'W'인 경우 윗면이 흰색이라는 의미입니다.』

[출력값 설명]
『한 행 또는 한 열에 놓인 N개의 바둑돌을 모두 뒤집는 작업들을 무한정 수행할 수 있다고 했을 때,
윗면이 흰색이 되는 바둑돌의 최소 개수를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
3
BBW
WBB
WBW

예제 출력1
2

예제 입력2
2
BW
WB

예제 출력2
0

예제 입력3
8
WWWBBBWW
BWBBBBBB
BWBWWWWW
WWWWBBWW
WBWWWBBW
BWWWWWWW
BBBWBBBW
BWWWBBWW

예제 출력3
17
'''
# -*- coding: utf-8 -*-
# 8527. 리버스 게임
import sys
input = sys.stdin.readline

def find_index(lst, k):
    l = lst
    i = 0
    idx = []
    while True:
        try:
          n = l.index(k)
          idx.append(n+i)
          i = n+i+1
          l = lst[i:]
        except:
            break
    return idx

if __name__ == "__main__":
    N = int(input())
    board = [list(input().rstrip()) for _ in range(N)]

    board_1d = [i for row in board for i in row]
    answer = board_1d.count('W')
    chk = 0
    row_prev_idx = []
    col_prev_idx = []
    
    while True:
        row_W_num = []
        for row in board:
            row_W_num.append(row.count('W'))

        board_conv = list(zip(*board))
        col_W_num = []
        for col in board_conv:
            col_W_num.append(col.count('W'))
        
        maxW = max(max(row_W_num), max(col_W_num))
        if row_W_num.count(maxW) >= col_W_num.count(maxW):
            row_idx = find_index(row_W_num, maxW)
            if row_idx == row_prev_idx:
                n_row += 1
            else:
                row_prev_idx = row_idx
                n_row = 0
                
            if n_row >= len(row_idx):
                break
            
            board[row_idx[n_row]] = ['B' if el == 'W' else 'W' for el in board[row_idx[n_row]]]
        else:
            col_idx = find_index(col_W_num, maxW)
            if col_idx == col_prev_idx:
                n_col += 1
            else:
                col_prev_idx = col_idx
                n_col = 0
            
            if n_col >= len(col_idx):
                break
            
            board_conv[col_idx[n_col]] = ['B' if el == 'W' else 'W' for el in board_conv[col_idx[n_col]]]
            board = list(zip(*board_conv))
            
        board_1d = [i for row in board for i in row]
        numW = board_1d.count('W')
        if answer <= numW:
            chk += 1
        else:
            answer = numW
            chk = 0
        
        if chk == N:
            break
        
    print(answer)