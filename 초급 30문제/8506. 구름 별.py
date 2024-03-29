'''
별찍기 문제는 프로그래밍 기초 예제로 자주 등장합니다. 
그런데 이번에는 별을 구름 모양으로 출력하라는 과제를 받았습니다.

양의 정수 N이 입력될 때 크기가 N인 구름 별을 출력하는 프로그램을 작성하세요. 
구름 별의 모양은 다음과 같습니다.

크기가 2인 구름 별의 모양입니다.

**
 **

다음은 크기가 3인 구름 별의 모양입니다.

**
 **
  **
-------------------------------------------
[입력값 설명]
양의 정수 N이 입력됩니다. (1 ≤ N ≤ 20)

[출력값 설명]
크기가 N인 구름 별을 출력합니다.
--------------------------------------------------

예제 입력1
2

예제 출력1
**
 **

예제 입력2
3

예제 출력2
**
 **
  **

'''


import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline


if __name__=="__main__":
    N=int(input())
    for i in range(N):
        print(' '*i,'**')
