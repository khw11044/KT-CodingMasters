'''
두 직사각형의 IoU(Intersecton over Union)란 
(두 직사각형의 교집합의 넓이)/(두 직사각형의 합집합의 넓이) 로 정의됩니다.

x-y 직교 좌표계 위의 모든 변이 x, y 축과 평행한 직사각형들의 정보가 주어집니다.
가장 큰 IoU 값을 가지는 직사각형의 쌍을 출력하는 프로그램을 작성하세요.

답이 여러개일 때 사전순으로 가장 앞서는 순서쌍을 출력합니다.
두 순서쌍 (x, y), (a, b) 에 대해 x < a 이거나 (x=a 이고 y < b) 일 때 (x, y)가 (a, b) 보다 사전순으로 앞선다고 표현합니다.
-------------------------------------------
[입력값 설명]
첫째줄에 정사각형의 개수를 의미하는 정수 N (2 ≤ N ≤ 20) 이 주어집니다.

둘째줄부터 N 개의 줄에 걸쳐 i (1 ≤ i ≤ N)번째 직사각형의 정보를 의미하는 네 정수 x, y, w, h
( -100 ≤ x, y ≤ 100, 1 ≤ w, h ≤ 100) 가 주어집니다.

x, y 는 직사각형 왼쪽 아래 꼭짓점의 좌표이고 w 는 밑변의 길이, h 는 높이를 의미합니다.

[출력값 설명]
가장 큰 IoU 값을 가지는 두 직사각형의 번호의 순서쌍을 공백으로 구분하여 출력하는 프로그램을 작성하세요.
직사각형의 번호는 1부터 시작하며, 순서쌍은 작은 번호부터 출력합니다.
--------------------------------------------------

예제 입력1
2
0 0 2 2
1 1 1 1

예제 출력1
1 2

예제 입력2
4
0 0 4 4
1 1 2 2
4 4 1 1
0 0 4 4

예제 출력2
14
'''

import sys

input=sys.stdin.readline

def max_iou(key_list,sq_dict,iou_list=[]):
    if len(key_list) == 1:
        iou_list.sort(key= lambda x : x[1], reverse=True)
        return iou_list[0][0]
    
    a = key_list[0]
    for b in key_list[1:]:
        if int(a) < int(b): key = a + ' ' + b
        else: key = b + ' ' + a
        inter = len(sq_dict[a]&sq_dict[b])
        iou = inter / (len(sq_dict[a])+len(sq_dict[b])-inter)
        iou_list.append([key,iou])
    return max_iou(key_list[1:],sq_dict,iou_list=iou_list)

if __name__ == "__main__":
    n = int(input())
    sq_list = [[i+1]+list(map(int, input().split())) for i in range(n)]
    sq_list.sort(key= lambda x : x[2])
    sq_list.sort(key= lambda x : x[1])

    sq_dict = {}
    for i in range(len(sq_list)):
        n,x,y,w,h = map(int,sq_list[i])
        sq = []
        for a in range(w):
            for b in range(h):
                sq.append((x+a,y+b))
        sq_dict[str(n)] = set(sq)

    print(max_iou(list(sq_dict.keys()),sq_dict))