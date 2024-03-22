'''
태국의 한 도시로 출장을 온 민혁은 택시를 타고 모든 마을을 방문하려 합니다.

이 도시의 택시 체계는 특이합니다.

각 택시는 어떤 두 마을 사이만 운행하므로,
어떤 택시를 타고 하나의 마을에서 출발해 다른 마을에 도착했다면 다른 택시로 갈아타야 합니다.

타고 싶은 택시들은 모두 전날에 선불로 요금을 내고 예약해야 합니다.
예약한 택시는 몇 번을 타더라도 추가비용 없이 자유롭게 이용할 수 있습니다.

도시에 N개의 마을과 M대의 택시가 있을 때, 
택시만으로 모든 마을을 방문하려면 택시 예약에 적어도 얼마가 드는지 출력하는 프로그램을 작성하세요. 
-------------------------------------------
[입력값 설명]
첫째 줄에 마을의 수 N(2 ≤ N ≤ 100)과 택시의 수 M(1 ≤ M ≤ 1,000)이 주어집니다.
이후 M개의 줄에 걸쳐 각 줄에 a, b, c가 공백을 구분으로 입력됩니다.
도시 a와 도시 b를 양방향으로 연결하는 예약비용이 c인 택시를 의미합니다. (a ≠ b, 1 ≤ a, b ≤ N, 1 ≤ c ≤ 100)
입력에서 주어진 도시를 정점으로, 택시 노선을 간선으로 가정하면 연결 그래프임을 보장합니다.

[출력값 설명]
택시만으로 모든 마을을 방문하려면 택시 예약에 적어도 얼마가 드는지 출력합니다.
--------------------------------------------------

예제 입력1
3 2
1 2 7
1 3 5

예제 출력1
12

예제 입력2
4 5
1 3 10
2 3 20
4 1 30
3 4 40
2 4 50

예제 출력2
60
'''

# Prim 알고리즘, 최소 스패닝 트리(Minimum Spanning Tree, MST)
# 이때, 이미 MST에 포함된 정점으로 연결하는 간선은 고려하지 않아 사이클을 방지합니다.

import sys
sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline

import heapq

def prim(graph, N):
    # 초기화
    visited = [False] * N
    minHeap = [(0, 0)]  # (cost, vertex)
    total_cost = 0

    while minHeap:
        cost, u = heapq.heappop(minHeap)
        if visited[u]:  # 두번째 방문이면 넘겨 
            continue

        visited[u] = True   # 첫방문 체크 
        total_cost += cost  # 현재 비용 추가 

        for v, c in graph[u]:
            if not visited[v]:
                heapq.heappush(minHeap, (c, v)) # cost를 기준으로 가장 낮은 c가 먼저 오게 됨

    return total_cost

if __name__=="__main__":
    N,M=map(int, input().split())   # N개의 마을, M대의 택시
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c=map(int, input().split()) # 도시a, 도시b, 예약비용 c
        a,b = a-1,b-1
        graph[a].append((b, c))
        graph[b].append((a, c))


    print(prim(graph, N))