'''
유한그룹 신입사원 공채모집의 서류심사와 면접심사가 모두 끝났습니다. 

인사과 직원들은 점수가 높은 사람들을 뽑아 채용하려고 합니다. 
심사기준은 서류심사와 면접심사에 대해서 두 부분 모두 점수가 높은 사람부터 등수를 매기는 것입니다. 
하지만 두 사람의 우열을 가릴 수 없는 경우에는 두 사람이 같은 등수라고 판단합니다. 

먼저 A의 서류점수와 면접점수가 각각 70점, 50점이고 B의 서류점수와 면접점수가 각각 83점, 60점이라면, 
서류점수와 면접점수가 둘 다 A보다 B가 높기 때문에 B가 더 높은 등수여야 합니다. 

또, A의 서류점수와 면접점수가 각각 53점, 62점이고 B의 서류점수와 면접점수가 각각 53점, 36점이라면, 
서류점수는 동일하지만 면접점수가 A가 B보다 더 높기 때문에 A가 더 높은 등수여야 합니다.


물론 면접점수만 같고 서류점수만 다른 경우에도 동일한 방식으로 등수가 매겨집니다.  


한편, A의 서류점수와 면접점수가 각각 37점, 96점이고 B의 서류점수와 면접점수가 각각 72점, 28점이라면, 
어느 한 쪽이 더 높다고 할 수 없으므로 이 둘은 같은 등수여야 합니다. 

마지막으로, 
A의 서류점수와 면접점수가 각각 68점, 73점, 
B의 서류점수와 면접점수가 각각 56점, 64점, 
C의 서류점수와 면접점수가 각각 71점, 56점이라고 해봅시다. 


A와 B만 보았을 때는 서로의 우열을 가릴 수 있지만, 
A와 C는 서로의 우열을 가릴 수 없고, 
B와 C도 서로의 우열을 가릴 수 없습니다.

이러한 경우에는 A, B, C 모두 같은 등수로 판정되어야 합니다. 

N명의 지원자들의 서류점수와 면접점수가 주어졌을 때, 
지원자들의 등수를 차례대로 출력하는 프로그램을 작성하세요. 
-------------------------------------------
[입력값 설명]
첫번째 줄에는 지원자의 수 N이 주어집니다.
그리고 이어지는 N개의 줄에는
각 지원자의 서류 점수와 면접 점수를 나타내는
자연수 x와 y가 공백을 구분으로 하여 각각 주어집니다.
(2 ≤ N ≤ 50, 10 ≤ x, y ≤ 200)

[출력값 설명]
첫번째 줄에 각 지원자들의 등수를 공백을 두고 입력받은 순서대로 출력합니다.
--------------------------------------------------

예제 입력1
2
62 53
36 53

예제 출력1
1 2

예제 입력2
5
68 73
56 64
71 56
15 23
18 22

예제 출력2
1 1 1 4 4

예제 입력3
5
60 65
40 60
50 70
30 50
35 40

예제 출력3
1 3 1 4 4

예제 입력4
5
80 90
75 85
70 80
65 75
90 60

예제 출력4
1 1 1 1 1
'''


# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline


# 특정 인덱스들을 전부 찾는 코드
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
# 다른 사람과 성적 관계 확인
def decide_level(i, j):
    s = 0
    if (score[i][0] > score[j][0]): s += 1
    elif (score[i][0] == score[j][0]): s == 0
    else: s -= 1
    
    if (score[i][1] > score[j][1]): s += 1
    elif (score[i][1] == score[j][1]): s == 0
    else: s -= 1
    
    return s
# 같은 등수가 되야하는 사람들 찾기
def find_same_level(s_level, i):
    for k in level_corr[i][1]:
        if (k not in s_level):
            s_level.append(k)
            s_level = find_same_level(s_level, k)
    return s_level

if __name__ == "__main__":
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    answer = [0] * N
    
    # 각 사람 간 점수 비교를 하는 level_corr 배열 만들기
    level_corr = []
    for i in range(N):
        win = 0
        same = []
        for j in range(N):
            if i == j:
                continue
            chk = decide_level(i, j)
            if chk > 0:
                win += 1
            elif chk == 0:
                same.append(j)
        # win : 해당 인덱스의 사람이 이기는 사람의 수 / same : 해당 인덱스의 사람과 같은 등수가 부여되야 하는 사람
        level_corr.append([win, same])
    
    level = 1
    while True:
        # 등수 부여가 안된 사람 찾기
        before_level = find_index(answer, 0)
        # 더 이상 등수 부여 안된 사람이 없으면 break
        if before_level == []:
            break

        # 부여 안된 사람 중 가장 높은 등수가 되야하는 사람 찾기
        front_p = -1 # 해당 사람 (인덱스 넘버) 저장
        front_n = -1 # 해당 사람이 높은 등수가 되는게 맞는지, win 저장
        for i in before_level:
            if level_corr[i][0] > front_n:
                front_n = level_corr[i][0]
                front_p = i
        
        # 일단 자기 자신은 무조건 해당 등수가 되야하므로, same 배열에 추가
        same = [front_p]
        same = find_same_level(same, front_p)
        for i in same:
            answer[i] = level
        level += len(same)
    
    print(*answer)