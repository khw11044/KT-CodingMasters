'''
자리 바꾸기 시간이 돌아왔습니다! 
담임 선생님인 철수는 N x 2 형태의 교실에 2N명의 학생을 앉혀야 합니다. 
학생들에게는 1번부터 2N번까지 번호가 붙어있습니다.

학생들을 어떤 방식으로 앉히느냐에 따라 교실의 분위기 점수가 결정됩니다. 
분위기 점수는 0에서 시작하고, i(1 ≤ i ≤ N)번 행에 앉은 두 학생의 관계가 좋으면 +1점, 보통이면 0점, 나쁘면 -1점이 분위기 점수에 더해집니다. 
어떤 두 학생의 관계가 좋지도 나쁘지도 않으면 두 학생의 관계는 보통입니다.

학생들을 적절히 배치하여 얻을 수 있는 분위기 점수의 최댓값을 구하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫째 줄에 교실의 행의 개수를 의미하는 양의 정수 N이 주어집니다. (1 ≤ N ≤ 4)

둘째 줄에 학생들의 관계의 개수를 의미하는 양의 정수 K가 주어집니다. (1 ≤ K ≤ N(2N-1))

이어서 K개의 줄에 걸쳐 학생들의 관계를 의미하는 양의 정수 a, b, c가 주어집니다.
a=1이면 b번 학생과 c번 학생의 관계가 좋음을 의미합니다.
a=2이면 b번 학생과 c번 학생의 관계가 나쁨을 의미합니다.
모순되는 관계는 입력으로 주어지지 않습니다.』

[출력값 설명]
『첫째 줄에 분위기 점수의 최댓값을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
1
1
1 2 1

예제 출력1
1

예제 입력2
2
2
1 1 2
2 3 4

예제 출력2
0
'''
# 8534. 자리 바꾸기
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    
    positive = []
    negative = []
    for _ in range(K):
        a, b, c = map(int, input().split())
        s1, s2 = min(b-1, c-1), max(b-1, c-1)
        if a == 1: positive.append((s1, s2))
        if a == 2: negative.append((s1, s2))
    
    students = list(range(2*N))
    combi = list(combinations(students, 2))
    combi = list(combinations(combi, N))
    
    seats = []
    for seat in combi:
        tmp = list(zip(*seat))
        tmp = set(tmp[0]+tmp[1])
        if len(tmp) == 2*N:
            seats.append(seat)
    
    answer = -N
    for seat in seats:
        chk = 0
        for s in seat:
            if s in positive:
                chk += 1
            if s in negative:
                chk -= 1
        answer = max(answer, chk)
    print(answer)