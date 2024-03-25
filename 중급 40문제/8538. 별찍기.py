

# 8538 별찍기
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
def star(n, x, y):
    if n == 1:
        arr[x][y] = a
        return
    n //= 3
    for i in range(3):
        for j in range(3):
            if (i + j) % 2 == 1:
                continue
            star(n, x + (n * i), y + (n * j))

if __name__=="__main__":
    n = int(input())
    a = '*'
    size = 3 ** (n-1)
    arr = [[' ' for _ in range(size)] for _ in range(size)]

    star(size, 0, 0)

    for i in range(size):
        print(''.join(arr[i]))