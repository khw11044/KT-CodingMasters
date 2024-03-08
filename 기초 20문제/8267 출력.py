'''
a,b,c를 각각 출력하세요

입력값 설명
정수 a,b,c가 주어집니다.

출력값 설명
a,b,c를 공백을 기준으로 출력합니다.
---------------------------------
예제 1
1 2 3 → 1 2 3
--------------
예제 2
4 5 6 → 4 5 6
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

print(a, b, c)