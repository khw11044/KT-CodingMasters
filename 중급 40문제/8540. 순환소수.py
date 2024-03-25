'''
모든 유리수는 유한소수나 순환소수로 표현 가능합니다. 

어떤 유리수가 입력되면 해당 유리수를 유한소수나 순환소수 형식으로 출력하는 프로그램을 작성하세요.

만약 주어진 유리수가 유한소수가 되는 경우, 해당 소수를 정확히 표현해야 합니다.
단, 끝에 불필요한 0이 존재해서는 안 됩니다. 

만약 주어진 유리수가 순환소수가 되는 경우,
순환마디는 중괄호로 묶어서 표현하고 그 순환마디의 길이는 최소가 되어야 합니다. 
또한, 순환마디의 시작지점은 가능한 가장 빠른 자릿수여야 합니다. 
-------------------------------------------
[입력값 설명]
첫 번째 줄에 분자를 의미하는 p와 분모를 의미하는 q가 주어집니다. (1 ≤ p < q ≤ 10,000)

[출력값 설명]
문제에서 주어진 형식으로 주어진 유리수를 유한소수 또는 순환소수 형식으로 출력합니다.
실수 오차는 허용하지 않음에 유의합니다.
--------------------------------------------------

예제 입력1
1 6

예제 출력1
0.1{6}

예제 입력2
3 5

예제 출력2
0.6

'''

import sys
# sys.stdin=open('input.txt', 'r')

def decimal_to_fraction(p, q):
    integer_part = p // q
    remainder = p % q
    decimals = []
    remainders = {}
    
    # 순환마디 찾기
    while (remainder != 0) and (remainder not in remainders):
        remainders[remainder] = len(decimals)
        remainder *= 10
        decimal_part = remainder // q
        decimals.append(decimal_part)
        remainder %= q
    
    # 결과 출력
    if remainder == 0:  # 유한 소수
        return f"{integer_part}." + "".join(map(str, decimals))
    else:  # 순환 소수
        cycle_start = remainders[remainder]
        non_cycle = ''.join(map(str, decimals[:cycle_start]))
        cycle = ''.join(map(str, decimals[cycle_start:]))
        return f"{integer_part}.{non_cycle}{{{cycle}}}"

if __name__ == "__main__":
    # 입력 및 출력
    p, q = map(int, input().split())
    print(decimal_to_fraction(p, q))