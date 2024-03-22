'''
구간 단속이란, 차량이 도로의 특정 구간을 통과하는데 걸린 시간과 
구간의 길이를 이용해 속도위반여부를 판정하는 방법입니다. 

구간을 통과하는데 걸린 시간은 
(차량이 구간 도착점의 카메라에 촬영된 시각 - 차량이 구간 출발점의 카메라에 촬영된 시각) 입니다.

두 카메라가 제공한 로그가 주어질 때,
각 차량의 속력을 meter / hour 단위로 출력하는 프로그램을 작성하세요.
-------------------------------------------
[입력값 설명]
첫 번째 줄에 구간의 길이가 meter 단위로 주어집니다. (1 ≤ 구간의 길이 ≤ 1000)
두 번째 줄에 두 카메라가 제공한 로그의 개수 N이 주어집니다. (1 ≤ N ≤ 3)
다음 N줄에 거쳐 출발점의 카메라가 제공한 로그가 주어집니다.
다음 N줄에 거쳐 도착점의 카메라가 제공한 로그가 주어집니다.
로그는 (차량번호 숫자 4자리) (촬영된 시각) 형식으로 제공되며, 시각은 HH:MM:SS 형식입니다.
(00 ≤ HH < 24, 00 ≤ MM, SS < 60)
모든 로그의 촬영일은 같으며, 같은 차량에 대해 출발점에서 촬영된 시각은 항상 도착점에서 촬영된 시각보다 앞섭니다.
한 카메라에 같은 차량번호가 두번 이상 주어지지 않습니다.
출발점의 카메라에 등장하는 차량은 반드시 도착점의 카메라에도 등장합니다.

[출력값 설명]
N개의 줄에 걸쳐 각 차량의 번호와 소수점을 버린 meter / hour 단위의 속력을 공백으로 구분하여 출력합니다.
차량 번호가 작은 것부터 출력해야 합니다.
--------------------------------------------------

예제 입력1
500
3
0000 20:00:05
5678 12:05:00
1243 07:59:00
5678 12:08:00
1243 08:01:32
0000 21:00:05

예제 출력1
0000 500
1243 11842
5678 10000

예제 입력2
1000
3
0000 00:00:00
1111 00:00:00
2222 00:00:00
0000 00:00:01
1111 00:01:00
2222 10:00:00

예제 출력2
0000 3600000
1111 60000
2222 100
'''


import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline
from collections import defaultdict

if __name__=="__main__":
    meter = int(input())    # 구간 거리 미터 
    N = int(input())    # log수 
    res = []
    
    start=defaultdict(str)
    for _ in range(N):
        # info = list(map(str, input().split()))
        # car_num = int(info[0])
        # start_time = list(map(int, info[1].split(':')))
        car_num, start_time = map(str, input().split())
        start[car_num] = start_time
        
    end=defaultdict(str)
    for _ in range(N):
        # info = list(map(str, input().split()))
        car_num, end_time = map(str, input().split())
        h_e,m_e,s_e = map(int, end_time.split(':'))
        h_s,m_s,s_s = map(int, start[car_num].split(':'))
        
        second = s_e - s_s
        minute = m_e - m_s
        hour = h_e - h_s
        
        if second<0:
            second = 60 + second
            minute -= 1
        
        if minute<0:
            minute = 60 + minute
            hour -= 1
            
        if hour<0:
            hour = 24 + hour
            
        # total = f'{hour:02d}:{minute:02d}:{second:02d}'
        total = (hour*60*60 + minute*60 +second) / (60*60)
        speed = int(meter / total)
        res.append([car_num, speed])
        
    
    res.sort(key=lambda x: x[0])
    for i in range(N):
        print(*res[i])