

import sys

input = sys.stdin.readline
def find_max(coin,max_array,h,n=1):
    if n == h:
        return max(max_array[n-1])
        
    for a in range(len(max_array[n-1])):
        for i in [a, a+1]:
            sum_coin = max_array[n-1][a] + coin[n][i]
            if sum_coin > max_array[n][i]: 
                max_array[n][i] = sum_coin

    return find_max(coin,max_array,h,n=n+1)

if __name__=="__main__":
    h = int(input())
    coin = [list(map(int, input().split())) for i in range(h)]

    max_array = [[0]*i for i in range(1,(h+1))]
    max_array[0][0] = coin[0][0]

    
    print(find_max(coin,max_array,h))



'''
import sys

n = int(input())
coins = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        coins[i][j] = temp[j]

for i in range(1, n):
    for j in range(i + 1):
        coins[i][j] += max(coins[i - 1][j - 1], coins[i - 1][j])

print(max(coins[-1]))

'''