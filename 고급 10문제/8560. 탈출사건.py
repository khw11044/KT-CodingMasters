'''
빈동은 동물원의 안전 책임자입니다.
동물원은 N행 M열의 격자, 총 N × M 칸으로 나눌 수 있습니다. 

어느 날 재규어들이 우리에서 탈출했습니다.
이 재규어들은 매우 공격적이라 당장 포획할 수 없습니다. 
빈동은 입장객들에게 대피하라고 알린 뒤, 날뛰는 재규어를 막을 방법을 찾아냈습니다.

동물원은 빈 칸, 재규어가 있는 칸, 울타리가 있는 칸으로 구분할 수 있습니다.
재규어들은 상하좌우 중 한 방향으로 인접한 빈 칸으로 이동할 수 있으며, 동물원 밖으로 나가지 못합니다.

빈동의 목표는 3개의 여분 울타리를  모두 설치해, 재규어가 도달할 수 없는 칸의 수를 최대화 하는 것입니다.
여분 울타리는 빈 칸에만 설치할 수 있고, 설치하면 그 칸은 울타리가 있는 칸이 됩니다.

빈동이 목표를 달성했을 때,
재규어가 도달할 수 없는 빈 칸의 수를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 동물원의 세로 크기 N과 가로 크기 M이 공백을 두고 주어집니다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N+1째 줄까지, 각 줄에 공백으로 구분된 M개의 숫자로 동물원의 상태가 주어집니다.
0은 빈 칸, 1은 울타리가 있는 칸, 2는 재규어가 있는 칸입니다.

주어진 동물원의 상태에 빈 칸은 3개 이상, 재규어는 1마리 이상 존재함이 보장됩니다.』

[출력값 설명]
『3개의 울타리를 모두 설치한 뒤 재규어로부터 안전한 빈 칸의 개수의 최댓값을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
4 4
0 1 0 0
1 0 2 0
0 1 0 0
0 0 1 1

예제 출력1
6

예제 입력2
6 4
1 1 0 1 
2 1 1 1 
1 2 2 0 
0 1 1 0 
2 0 1 1 
1 0 1 2 

예제 출력2
3
'''
# 1을 3개 더 0에 넣어서, 2가 움직이지 못하는 0의 갯수 출력하기

# 8560. 탈출사건 
import sys
input = sys.stdin.readline

# 기존의 index 함수는 위치를 1개만 찾으니 직접 만든다
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

# 1d 좌표 값을 2d 좌표 값으로 변환
def convert_2d(lst):
    l_2d = []
    for i in lst:
        l_2d.append((int(i/M), int(i%M)))
    return l_2d

# 재규어 무빙 가능 위치를 반환
def make_visited(v, y, x):
    if (y-1 >= 0):
        if ((zoo_2d[y-1][x]==0) & (v[y-1][x] == False)):
            v[y-1][x] = True
            v = make_visited(v, y-1, x)
    if (y+1 < N):
        if ((zoo_2d[y+1][x]==0) & (v[y+1][x] == False)):
            v[y+1][x] = True
            v = make_visited(v, y+1, x)
    if (x-1 >= 0):
        if ((zoo_2d[y][x-1]==0) & (v[y][x-1] == False)):
            v[y][x-1] = True
            v = make_visited(v, y, x-1)
    if (x+1 < M):
        if ((zoo_2d[y][x+1]==0) & (v[y][x+1] == False)):
            v[y][x+1] = True
            v = make_visited(v, y, x+1)
    return v

if __name__ == "__main__":
    N, M = map(int, input().split())
    zoo_2d = [list(map(int, input().split())) for _ in range(N)]
    zoo_1d = [i for row in zoo_2d for i in row]

    fence = find_index(zoo_1d, 1)

    jaguar = find_index(zoo_1d, 2)
    jaguar_xy = convert_2d(jaguar)

    visited_2d = [[False] * M for _ in range(N)]
    for (jy, jx) in jaguar_xy:
        visited_2d = make_visited(visited_2d, jy, jx)
    visited_1d = [i for row in visited_2d for i in row]

    p_fence = find_index(visited_1d, True)
    p_fence_xy = convert_2d(p_fence)

    answer = 0
    for i in range(len(p_fence_xy)-2):
        y1, x1 = p_fence_xy[i][0], p_fence_xy[i][1]
        zoo_2d[y1][x1] = 1
        for j in range(i+1, len(p_fence_xy)-1):
            y2, x2 = p_fence_xy[j][0], p_fence_xy[j][1]
            zoo_2d[y2][x2] = 1
            for k in range(j+1, len(p_fence_xy)):
                y3, x3 = p_fence_xy[k][0], p_fence_xy[k][1]
                zoo_2d[y3][x3] = 1

                visited_2d = [[False] * M for _ in range(N)]
                for (jy, jx) in jaguar_xy:
                    visited_2d = make_visited(visited_2d, jy, jx)
                visited_1d = [i for row in visited_2d for i in row]

                for i in fence:
                    visited_1d[i] = True
                for i in jaguar:
                    visited_1d[i] = True

                safe_zone = visited_1d.count(False) - 3
                answer = max(answer, safe_zone)

                zoo_2d[y3][x3] = 0
            zoo_2d[y2][x2] = 0
        zoo_2d[y1][x1] = 0
    print(answer)