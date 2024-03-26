'''
교실은 N행 M열의 격자,
총 N × M 칸으로 나눌 수 있고, 모든 칸은 정사각형입니다. 

각 칸의 중앙에는 학생이 한 명씩 있습니다.
모든 학생은 각자 자신이 좋아하는 수가 적힌 종이를 들고 있습니다.

선생님은 서로 같은 수가 적힌 종이를 들고 있는 
서로 다른 4명의 학생의 위치를 네 꼭짓점으로 하는 정사각형들을 만들었습니다. 

단, 정사각형의 변은 교실의 벽 중 하나와 평행해야 합니다. 

선생님이 만든 정사각형들 중 가장 넓은 것의 넓이를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 교실의 세로 크기 N과 가로 크기 M이 공백을 구분으로 주어집니다.
N과 M은 2 이상 50 이하의 정수입니다.

둘째 줄부터 N+1째 줄까지 각 줄에 M개의 수가 공백을 구분으로 주어집니다.
i+1째 줄의 j번째 수는 격자의 i행 j열에 있는 학생이 좋아하는 수 입니다.

모든 학생은 1 이상 100 이하의 정수 중 하나를 좋아하며,
선생님이 하나 이상의 정사각형을 만들 수 있음을 보장합니다.』

[출력값 설명]
『선생님이 만든 정사각형들 중 가장 넓은 것의 넓이를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
5 5
9 8 1 6 5
9 8 7 6 5
1 8 2 2 1
9 8 2 2 5
9 8 1 6 5

예제 출력1
4

예제 입력2
4 5
6 5 2 3 5
4 2 4 2 3
4 7 8 9 8
4 5 1 1 5

예제 출력2
16
'''
# -*- coding: utf-8 -*-
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

# lst_2d 가 들어오면 해당 리스트에서 만들 수 있는 정사각형의 최대 넓이를 반환
def find_squre(lst):
    if len(lst) < 4:
        return 0
    answer = 0
    for i in range(len(lst)-3):
        y1, x1 = lst[i][0], lst[i][1]
        for j in range(i+1, len(lst)-2):
            y2, x2 = lst[j][0], lst[j][1]
            if y2==y1:
                n = x2-x1
                for k in range(j+1, len(lst)-1):
                    y3, x3 = lst[k][0], lst[k][1]
                    if (x3==x1) & ((y3-y1)==n):
                        for l in range(k+1, len(lst)):
                            y4, x4 = lst[l][0], lst[l][1]
                            if ((y4==y3) & (x4==x2)):
                                answer = max(answer, (n+1)*(n+1))
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    cls = [list(map(int, input().split())) for _ in range(N)]
    # 특정값 위치를 찾기 위해 1차원 배열 변환
    cls = [i for row in cls for i in row]

    answer = 0
    for k in range(1, max(cls)+1):
        c_lst = find_index(cls, k)
        lst_2d = []
        for c in c_lst:
            lst_2d.append((int(c/M), int(c%M)))
        # 2차원 배열로 변환 완료
        answer = max(answer, find_squre(lst_2d))
    print(answer)