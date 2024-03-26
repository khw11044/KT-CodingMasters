'''
화가인 지연은 그림판에서 N x M 크기의 격자판을 칠하여 그림을 그렸습니다.
각 칸은 검정색, 빨간색, 파란색 3개의 색 중 하나로 칠해져 있거나 빈 칸입니다.
그림은 얼핏 보면 검정색으로 구분된 여러 개의 영역으로 나뉜 것 같아 보입니다.
이때 검정색이 아닌 두 칸이 상하좌우로 인접하다면 하나의 영역에 속하는 것으로 간주합니다.

그림을 유심히 보던 지연은 같은 영역 안에 있는 색들을 하나의 색으로 통일하고 싶었습니다.
그래서 다음과 같이 각각의 영역을 수정하기로 했습니다.

하나의 영역에 대해,
i) 빨간색과 파란색으로 칠해져 있는 칸의 수가 동일하거나, 파란색으로 칠해져 있는 칸이 더 많다면 빨간색으로 칠해져 있는 칸의 색깔을 지우고 빈 칸으로 만듭니다.
ii) 빨간색으로 칠해져 있는 칸이 더 많다면 이번에도 역시 파란색으로 칠해져 있는 칸의 색깔을 지우고 빈 칸으로 만듭니다.

그림의 정보가 주어질 때, 지연이 수정 작업을 끝내고 그림에 남은 빨간색 칸, 파란색 칸의 개수를 각각 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫 줄에는 두 정수 N과 M이 주어지며(3 ≤ N, M ≤ 100),
각 수는 그림의 행과 열의 수를 의미합니다.

둘째 줄부터 N개의 줄에 그림이 주어집니다.
i번째 줄의 j번째 문자는 그림의 i행 j열의 정보를 의미하며 다음 중 하나입니다.

A : 빨간색으로 칠해져 있는 칸
B : 파란색으로 칠해져 있는 칸
O : 빈 칸
X : 검정색으로 칠해져 있는 칸』

[출력값 설명]
『첫째 줄에 지연이가 수정 작업을 끝내고 그림에 남은 빨간색 칸, 파란색 칸의 개수를 순서대로 공백을 두고 출력합니다.』
------------------------------------------------------------------------
예제 입력1
4 4
AXBB
BXAA
XABX
OOBX

예제 출력1
0 5

예제 입력2
5 6
OAABOX
XXXXXX
XABAOB
XOBOAB
XOBABA

예제 출력2
2 6
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque

def solution(y, x):
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] # (y, x) 방향
    q = deque()
    q.append((y, x))
    
    a, b = 0, 0
    while q:
        y, x = q.popleft()
        if visited[y][x] == False:
            if canvas[y][x] == 'A': a += 1
            elif canvas[y][x] == 'B': b += 1
            visited[y][x] = True
            
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if (0 <= ny < N) and (0 <= nx < M):
                    if (canvas[ny][nx] != 'X') and (visited[ny][nx] == False):
                        q.append((ny, nx))
    if a <= b:
        return 0, b
    else:
        return a, 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    canvas = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    A, B = 0, 0
    for y in range(N):
        for x in range(M):
            if (canvas[y][x] != 'X') and (visited[y][x] == False):
                a, b = solution(y, x)
                A += a
                B += b
    print(A, B)