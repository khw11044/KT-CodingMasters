'''
피자집 사장인 현석은 대한민국 화폐 단위와 같은 쿠폰을 만들어
손님들이 현금으로 결제할 때 거스름돈 대신 쿠폰으로 거슬러 줍니다. 

하지만 최근 쿠폰이 모자라진 현석은 손님들에게 거슬러 주는 쿠폰의 개수를 가능한 적게 하려고 합니다.

현석이 거슬러주어야 하는 금액이 주어지면, 
그 금액에 맞추어 거슬러줄 때 쿠폰이 최소 몇 장 필요한지 출력하는 프로그램을 작성하세요. 
(쿠폰은 대한민국 화폐 단위와 동일하게 10원, 50원, 100원, 500원, 1000원, 5000원, 10000원, 50000원짜리가 있습니다.)
------------------------------------------------------------------------
[입력값 설명]
『현석이가 거슬러주어야 하는 금액 N이 입력됩니다. (10 ≤ N ≤ 1,000,000)

N은 10의 배수임을 보장합니다.』

[출력값 설명]
『필요한 쿠폰 개수의 최솟값을 출력합니다.』
------------------------------------------------------------------------
예제 입력1
5630

예제 출력1
6

예제 입력2
102830

예제 출력2
11
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

if __name__=="__main__":
    N=int(input())
    cnt=0
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for m in moneys:
        cnt += N//m
        N=N%m
    
    print(cnt)