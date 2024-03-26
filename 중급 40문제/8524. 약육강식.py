'''
은진의 수족관에는 여러 마리의 상어가 일렬로 늘어서 있습니다. 
또한 상어마다 크기가 정해져 있습니다. 
뒤에 있는 상어가 앞에 있는 상어보다 크기가 크다면 뒤에 있는 상어가 앞에 있는 상어를 삼킬 수 있습니다.

예를 들어 상어의 크기가 순서대로 (3, 5, 1, 2, 3, 8)이라면 
크기가 3인 상어를 5인 상어가 먹고, 5인 상어를 8인 상어가 먹을 수 있습니다. 
이 때 연속적으로 먹히는 관계에 포함되는 상어는 총 3마리가 됩니다.

반면에 크기가 1인 상어를 2인 상어가 먹고, 
크기가 2인 상어를 3인 상어가 먹고, 
크기가 3인 상어를 8인 상어가 먹는다면 
연속적으로 먹히는 관계에 포함되는 상어는 총 4마리가 됩니다.

상어들의 크기가 주어졌을 때 
연속적으로 먹히는 관계를 가진 상어들의 최대 마리 수를 구하는 프로그램을 작성하세요.
------------------------------------------------------------------------
[입력값 설명]
『첫 번째 줄은 상어의 마리 수 N이 입력됩니다. (1 ≤ N ≤ 100)
두 번째 줄에는 각 상어의 크기가 1 이상 100 이하의 정수로 공백을 기준으로 순서대로 입력됩니다.』

[출력값 설명]
『은진의 수족관에서 연속적으로 먹히는 관계를 가진 상어들의 최대 마리 수를 출력합니다.』
------------------------------------------------------------------------
예제 입력1
6
3 5 1 2 3 8

예제 출력1
4

예제 입력2
10
1 2 3 4 5 6 7 10 8 8

예제 출력2
8

예제 입력3
8
1 2 3 6 4 5 7 8

예제 출력3
7

예제 입력4
8
8 1 5 3 4 2 7 6

예제 출력4
4
'''
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# LIS 알고리즘 : 이분탐색을 활용한 방식 (시간복잡도 : O(NlogN))
def b_search(target, lis):
    start, end = 0, len(lis) - 1
    while start < end:
        mid = (start + end) //2
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]:
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start
# 정확히 원하는 수열이 나오는 것이 아닌, 단순 크기 비교를 해서 답을 도출해내는 알고리즘
if __name__ == "__main__":
    N = int(input())
    aquarium = list(map(int, input().split()))

    answer = [aquarium[0]]
    for i in range(1, N):
        shark = aquarium[i]
        if answer[-1] < shark:
            answer.append(shark) # 현재 비교하는 값이 더 크면 그냥 더해준다
        else: # 그게 아니라면 지금 값이 들어갈 수 있는 적합한 위치를 찾음
            idx = b_search(shark, answer)
            answer[idx] = shark
    
    print(len(answer))
#########################################################################
# # LIS 알고리즘 : 동적 할당을 활용한 방식 (시간복잡도 : O(N**2))
# if __name__ == "__main__":
#     N = int(input())
#     aquarium = list(map(int, input().split()))

#     DP = [1] * N # 인덱스 값 기준 자기 앞에 얼마나 먹을 수 있는지 (생성되는 사슬 길이)
#     for i in range(1, N):
#         for j in range(i): # 자기 앞하고만 비교
#             if aquarium[j] < aquarium[i] and DP[i] < DP[j] + 1:
#                 DP[i] = DP[j] + 1 # 먹을 수 있는 상어가 생성해둔 사슬이 현재 자기보다 길면, 자기 자신(+1) 포함 해당 사슬 길이로 변경
#     print(max(DP))
#########################################################################
# # 제출용으로 작성한 코드
# class Node:
#     def __init__(self, value, cnt = 0):
#         self.value = value
#         self.depth = cnt
#         self.child = []

# class Tree:
#     def __init__(self, root):
#         self.root = Node(root)

#     def insert(self, node, value):
#         global answer
#         # 현재 노드 아래로 자식 노드가 없을 때
#         if (node.child == []):
#             c_node = Node(value, node.depth+1)
#             node.child.append(c_node)
#             answer = max(answer, node.depth+1)
#         else:
#             # 아래로 자식 노드가 있을 때
#             chk = 0 # 자식 노드들 중 하나라도 들어갔는지 확인하기 위한 변수
#             for n in node.child:
#                 if n.value > value:
#                     self.insert(n, value)
#                     chk = 1
#             # 자식 노드들 체크 했는데, 전부 현재 값보다 커서 그 아래로 못 넣었다면 현재 노드에 자식 노드로 넣기
#             if chk == 0:
#                 c_node = Node(value, node.depth+1)
#                 node.child.append(c_node)
#                 answer = max(answer, node.depth+1)

# if __name__ == "__main__":
#     N = int(input())
#     aquarium = list(map(int, input().split()))
#     answer = 0
#     # 가장 상위 포식자 하나 넣기 (최대값이 100이라서 101로 입력)
#     chain = Tree(101)
#     for shark in range(len(aquarium) - 1, -1, -1):
#         chain.insert(chain.root, aquarium[shark])
#     print(answer)
#########################################################################
# if __name__ == "__main__":
#     N = int(input())
#     aquarium = list(map(int, input().split()))

#     answer = 0
#     end = aquarium.index(min(aquarium)) + 1

#     for start in range(end):
#         chains = [[start]]
#         for comparison in range(start+1, N):
#             for chain in chains:
#                 if aquarium[chain[-1]] < aquarium[comparison]:
#                     chain.append(comparison)
#                 else:
#                     for i in range(len(chain)-2, -1, -1):
#                         if aquarium[chain[i]] < aquarium[comparison]:
#                             new_chain = chain[:i+1] + [comparison]
#                             chains.append(new_chain)
#                             break
#         long_chain = 0
#         for chain in chains:
#             long_chain = max(long_chain, len(chain))
#         answer = max(answer, long_chain)
#     if answer == 1: answer = 0
#     print(answer)
#########################################################################
# if __name__ == "__main__":
#     N = int(input())
#     sharks = list(map(int, input().split()))
#     answer = 0

#     visited = [False] * N
#     q = deque()
#     for i in range(N):
#         q.append([i])
#         while q:
#             chain = q.popleft()
#             s = chain[-1]
#             visited[s] = True
#             for j in range(s+1, N):
#                 if (sharks[s] < sharks[j]) and (visited[j] == False):
#                     q.append(chain+[j])
#             answer = max(answer, len(chain))
#     if answer == 1: answer = 0
#     print(answer)
#########################################################################
# if __name__ == "__main__":
#     N = int(input())
#     sharks = list(map(int, input().split()))
#     answer = 0

#     q = deque()
#     for i in range(N):
#         q.append([i])
#         while q:
#             chain = q.popleft()
#             s = chain[-1]
#             p = []
#             for j in range(s+1, N):
#                 if sharks[s] < sharks[j]:
#                     p.append((j, sharks[j]))
#             if len(p) == 0:
#                 answer = max(answer, len(chain))
#             else:
#                 if len(p) == 1:
#                     q.append(chain+[p[0][0]])
#                 else:
#                     # 가장 가까운 놈이 먹을 경우 체크해보기
#                     q.append(chain+[p[0][0]])
#                     # 가장 작은 놈이 먹을 경우 체크해보기
#                     p.sort(key=lambda x: x[1])
#                     q.append(chain+[p[0][0]])
#     if answer == 1: answer = 0
#     print(answer)