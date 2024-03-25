'''
콩벌레는 보고 있는 방향에 장애물이 없으면 전진하다가 장애물을 만나면 좌우로 방향을 꺾는 습성이 있습니다.

이때, 최초의 장애물을 만날 때는 반시계 방향으로 꺾고, 
다음 장애물을 만날 때마다는 기존에 반시계 방향으로 꺾었을 경우 시계 방향으로, 
기존에 시계 방향으로 꺾었을 경우 반시계 방향으로 꺾습니다.

콩벌레의 위치와 보고 있는 방향이 주어졌을 때 콩벌레가 10 × 10 지도를 빠져나갈 수 있는지 판단하는 프로그램을 작성하세요.
콩벌레가 지도 상에서 사라지면 지도를 빠져나간 것으로 간주합니다.
-------------------------------------------
[입력값 설명]
첫째줄부터 10개의 줄에 걸쳐 미로의 상태가 주어집니다.
0은 빈 공간을, 1은 벽을, 2는 콩벌레를 나타냅니다.
공벌레는 초기에 위로 진행합니다.

[출력값 설명]
콩벌레가 지도를 빠져나갈 수 있으면 yes, 없으면 no를 출력합니다. (반드시 소문자로 출력하셔야 합니다.)
--------------------------------------------------

예제 입력1
1111111111
0000020000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
1111111111

예제 출력1
yes

예제 입력2
1111111111
0000120000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
1111111111

예제 출력2
no
'''


import sys


def generation(n,cell,c=0):
    if n == c:
        return cell
        
    next_gen_cell = [[0]*5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            check_ind = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x-1],[y,x+1],[y+1,x-1],[y+1,x],[y+1,x+1]]
            check_ind = [k for k in check_ind if (k[0]>=0)&(k[1]>=0)&(k[0]<=4)&(k[1]<=4)]
            check_live = 0
            for ind in check_ind:
                check_live += int(cell[ind[0]][ind[1]])
            
            if int(cell[y][x]) == 1:
                if check_live in [2,3]:
                    next_gen_cell[y][x] = 1
            else:
                if check_live == 3:
                    next_gen_cell[y][x] = 1
            # print(f'({y},{x}) cell[y][x] {check_live}')
    return generation(n,next_gen_cell,c=c+1)

if __name__ == "__main__":
    n = int(input())
    cell = [input() for _ in range(5)]

    for nums in generation(n,cell):
        print(''.join(map(str,nums)))
