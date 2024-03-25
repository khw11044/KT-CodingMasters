

import sys
# sys.stdin=open('input.txt', 'r')
input=sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    arr = [0] * (n+1)
    arr[2] = 1

    for i in range(3, n+1):
        arr[i] = arr[i-1] + 2
        
    print(arr[n])