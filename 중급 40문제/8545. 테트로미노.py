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
sys.setrecursionlimit(100000)


def is_tetro(y,x,input_array,check_array):
    s_ind = [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]
    s_ind = [ind for ind in s_ind if (ind[0]>=0)&(ind[1]>=0)&(ind[0]<=4)&(ind[1]<=4)]
    n = 0
    for ind in s_ind:
        if (input_array[ind[0]][ind[1]] == '#') and (check_array[ind[0]][ind[1]] == False):
            # print('ind',ind[0], ind[1] )
            check_array[ind[0]][ind[1]] = True
            k, check_array = is_tetro(ind[0],ind[1],input_array,check_array)
            n += (1 + k)
    return n, check_array

if __name__ == "__main__":

    input_array = [input() for _ in range(5)]
    check_array = [[False]*5 for _ in range(5)]

    x = 0    
    for y in range(5):
        x += list(input_array[y]).count('#')

    if x != 4:
        ans = 'NO'
    else:
        for y in range(5):
            x =input_array[y].find('#')
            if x >-1: break
        # print(y, x)
        n, check_array = is_tetro(y,x,input_array,check_array)
        if n == 4: ans ='YES'
        else:  ans = 'NO'
    print(ans)