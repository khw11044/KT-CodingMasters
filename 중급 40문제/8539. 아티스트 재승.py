'''
재승은 길이가 K인 문자열을 이용해 N행 M열의 사각형 격자 위에 그림을 그렸다고 주장하고 있습니다. 
재승의 말에 따르면, 그림을 그린 방법은 다음과 같습니다.

1. 아무 칸이나 골라 첫번째 문자를 쓴다.
2. i ( 2 ≤ i ≤ K )번째 문자는 i-1번째 문자를 쓴 칸과 한 변을 공유하는 칸들 중 하나를 선택해 쓴다. 
단, 격자를 벗어나거나 이미 문자가 쓰여있는 칸을 선택하는 것은 불가능하다.
3. 그림을 그리는 과정에서 문자열의 순서에 따라 이미 사용한 문자는 다시 사용할 수 없다.


위와 같이 그림을 완성하면 격자에 문자가 적힌 칸은 K개, 그렇지 않은 칸은 N×M - K개임을 알 수 있습니다.
문자열이 주어지면 재승의 방법대로 같은 그림을 그릴 수 있는지 알려주는 프로그램을 작성하세요.

-------------------------------------------
[입력값 설명]
첫 번째 줄에 길이가 K인 문자열이 주어집니다. (1 ≤ K ≤ 10)
문자열은 'a'부터 'z'까지의 영어 알파벳 소문자로만 이루어져 있습니다.

두 번째 줄에 격자의 크기를 나타내는 N과 M이 공백을 구분으로 주어집니다. (1 ≤ N, M ≤ 10)
다음 N개의 줄에 줄 당 M개의 문자로 그림이 주어집니다.
'.' (아스키코드 46) 은 문자가 쓰여있지 않은 칸을, 'a', 'b', 'c', … 'z'는 해당하는 알파벳이 쓰여있는 칸을 의미합니다.
그 밖의 다른 문자는 주어지지 않습니다

[출력값 설명]
주어진 문자열을 이용해 재승의 방법대로 같은 그림을 그릴 수 있다면, 첫번째 문자가 쓰여있을 수 있는 칸의 개수를 출력합니다.
그렇지 않은 경우 0을 출력합니다.

--------------------------------------------------

예제 입력1
aaab
3 2
aa
ab
..

예제 출력1
2

예제 입력2
abcdefg
2 4
ae..
ro..

예제 출력2
0

'''

import sys
sys.stdin=open('input.txt', 'r')

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(nx,ny):
    return 0<=nx<N and 0<=ny<M

def DFS(x, y, index, visited):
    if index == len(word):
        return 1

    for dx, dy in zip(dxs, dys):
        nx = x+dx
        ny = y+dy
        if in_range(nx,ny) and not visited[nx][ny] and picture[nx][ny] == word[index]:
            visited[nx][ny] = True
            if DFS(nx, ny, index + 1, visited):
                return 1
            visited[nx][ny] = False  # 이전 상태로 되돌리기
    return 0


if __name__ == "__main__":
    word = input().strip()
    N, M = map(int, input().split())
    
    # 격자 크기가 단어 길이보다 작은 경우 바로 0 출력
    if N * M < len(word):
        print(0)
        sys.exit()
        
    picture = [list(input().strip()) for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(M):   # 그리드 완전 탐색
            if picture[i][j] == word[0]:   # 첫단어
                visited = [[False for _ in range(M)] for _ in range(N)]
                visited[i][j] = True
                count += DFS(i, j, 1, visited)
    
    print(count)