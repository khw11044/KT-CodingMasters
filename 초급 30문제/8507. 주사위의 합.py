'''
주사위 2개를 굴려 합이 N이 나오는 경우의 수를 구하는 프로그램을 작성하세요. 

반드시 주사위 2개를 함께 굴리며, 
예를 들어 N = 5일 때는 (1, 4), (2, 3), (3, 2), (4, 1)의 네 가지 경우의 수가 존재합니다.
-------------------------------------------
[입력값 설명]
정수 N이 입력됩니다. (2 ≤ N ≤ 12)

[출력값 설명]
주사위 2개를 굴려 합이 N이 나오는 각각의 경우를 출력합니다.
출력할 때는 첫 번째 주사위의 눈금이 오름차순으로 출력될 수 있도록 합니다.
--------------------------------------------------

예제 입력1
5

예제 출력1
1 4
2 3
3 2
4 1

예제 입력2
7

예제 출력2
1 6
2 5
3 4
4 3
5 2
6 1
'''


import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline


if __name__=="__main__":
    N=int(input())
    for i in range(1,7):
        for j in range(1,7):
          if sum([i,j])==N:
            print(i,j)