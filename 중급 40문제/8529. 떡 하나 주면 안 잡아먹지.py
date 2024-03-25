'''
떡장사를 마치고 집에 가는 아낙네에게는 집에서 엄마를 애타게 기다리는 사랑스러운 오누이가 있습니다.
집에 가는 길은 N행 N열, 총 N × N 칸의 격자로 나뉘며,
모든 칸에는 호랑이가 한 마리씩 살고 있습니다.
이 호랑이들은 떡을 매우 좋아하여 "떡 몇 개 주면 안 잡아먹지!"라며 위협을 합니다.

제일 왼쪽 위 1행 1열의 칸에 서 있는 아낙네는 제일 오른쪽 아래 N행 N열의 칸에 있는 집으로 돌아가야 합니다.
아낙네는 상하좌우 중 한 방향으로 인접한 칸으로만 이동할 수 있으며,
길 밖으로 나가는 것은 불가능합니다.

집에 가는 길에 만나는 모든 호랑이에게 반드시 원하는 만큼의 떡을 줘야 하며,
이는 1행 1열의 호랑이와 N행 N열의 호랑이를 포함합니다.
아낙네가 집으로 돌아가려면 최소 몇 개의 떡이 필요한지 출력하는 프로그램을 작성하세요.

-------------------------------------------
[입력값 설명]
첫째 줄에 정수 N이 주어집니다. (2 ≤ N ≤ 50)

둘째 줄부터 N개의 줄에 걸쳐 각 칸의 호랑이가 요구하는 떡의 개수가 주어집니다.
둘째 줄의 첫 번째 수가 1행 1열이고, N+1째 줄의 N번째 수가 N행 N열입니다.

[출력값 설명]
아낙네가 집으로 돌아가려면 최소 몇 개의 떡이 필요한지 출력합니다.
--------------------------------------------------

예제 입력1
3
1 4 6
2 7 4
4 5 2

예제 출력1
14

예제 입력2
5
3 62 5 1 8
5 73 9 38 9
1 80 2 92 7
2 59 4 67 4
6 7 3 87 4

예제 출력2
80
'''

import sys
# sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline
from collections import deque

dxs = [1,0,0,-1]
dys = [0,1,-1,0]

def in_range(nx,ny):
    return 0<=nx<N and 0<=ny<N

if __name__=="__main__":
    N=int(input())
    MAX_SIZE = sys.maxsize
    board = [list(map(int, input().split())) for _ in range(N)]
    recode = [[MAX_SIZE]*N for _ in range(N)]
    
    
    recode[0][0]=board[0][0]
    Q = deque()
    Q.append([0,0])
    while Q:
        x,y = Q.popleft()
        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny):
                if recode[nx][ny]>recode[x][y]+board[nx][ny]:
                    recode[nx][ny] = recode[x][y]+board[nx][ny]
                    Q.append([nx,ny])
    
    print(recode[N-1][N-1])
    
    