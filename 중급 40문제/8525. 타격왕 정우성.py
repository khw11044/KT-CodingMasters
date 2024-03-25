

import sys

input = sys.stdin.readline

def find_k(x,y,rate):
    if rate >= 99:
        return -1
        
    k = (y - ((rate+1)/100)*x)/((rate+1)/100 - 1)

    if k >= 10**9 or k < 0:
        return -1
    elif int(k)<k:
        return int(k) + 1

if __name__=="__main__":
    x,y = map(int, input().split())
    rate = (y*100)//x

    print(int(find_k(x,y,rate)))