

import sys
from collections import deque

def find_min_steps(N, K):
    visited = [False] * 100001  # 방문 여부를 저장하는 리스트
    queue = deque([(K, 0)])  # 시작 숫자와 횟수를 저장하는 큐
    visited[K] = True

    while queue:
        num, steps = queue.popleft()

        if num == N:  # 목표 숫자에 도달한 경우 횟수 반환
            return steps

        # 다음에 방문할 숫자를 추가
        next_num = [num + 1, num - 1, num * 2]
        for nxt in next_num:
            if 0 <= nxt <= 100000 and not visited[nxt]:
                queue.append((nxt, steps + 1))
                visited[nxt] = True


if __name__=="__main__":
    N, K = map(int, input().split())
    print(find_min_steps(N, K))