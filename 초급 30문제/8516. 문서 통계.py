'''
많은 워드프로세서들은 문서에 대한 통계를 제공합니다.

한 줄 분량의 문서가 주어졌을 때, 
이 문서에 대한 통계를 출력하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『문서의 내용이 주어집니다.

문서는 100자 이내의 문자열이며, 알파벳 대문자와 소문자, 공백으로만 이루어져 있습니다.
문자열의 맨 처음과 맨 마지막 글자는 공백 문자가 아닙니다.』

[출력값 설명]
『첫째 줄에 공백을 포함한 글자 수를 출력합니다.

둘째 줄에 공백을 제외한 글자 수를 출력합니다.

셋째 줄에 단어의 수를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
Coding Masters

예제 출력1
14
13
2

예제 입력2
A B  C D   E

예제 출력2
12
5
5
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    doc = input().rstrip()
    print(len(doc))                     # 공백을 포함한 글자수 
    print(len(doc.replace(' ','')))     # 공백을 제외한 글자수 
    print(len(doc.split()))             # 단어의 수 