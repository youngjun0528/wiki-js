#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

# 1자리 숫자
# 1, 2, 3, 4, 5, 6, 7, 8, 9

# 2자리 숫자
# 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 88, 98

# 3자리 숫자
# 101, 121, 123, 212, 210, 232, 234 ....

num = [[0]*10]*100
num[1][0] = 0
num[1][1] = 1
num[1][2] = 1

# 마지막 숫자에 -1 , +1 한 값이 붙어야 한다.

# 2자리 수를 만드는 경우는
# 1자리 수 중에서 끝 자리가 0 인 경우 1자리 숫자 중 + 1 한 경우의 수 더하기
num[2][0] = num[1][1]
# 1자리 수 중에서 끝 자리가 1 인 경우 1자리 숫자 중 - 1, + 1 한 경우의 수 더하기
num[2][1] = num[1][0] + num[1][2]
# 1자리 수 중에서 끝 자리가 9 인 경우 1자리 숫자 중 - 1 한 경우의 수 더하기
num[2][9] = num[1][8]

# 3자리 수를 만드는 경우는
# 2자리 수 중에서 끝 자리가 0 인 경우 2자리 숫자 중 + 1 한 경우의 수
num[3][0] = num[2][1]
# 2자리 수 중에서 끝 자리가 1 인 경우 2자리 숫자 중 - 1 , + 1 한 경우의 수
num[3][1] = num[2][0] + num[2][2]
# 2자리 수 중에서 끝 자리가 9 인 경우 2자리 숫자 중 - 1 , + 1 한 경우의 수
num[3][1] = num[2][8]

# num[K][L] = num[K-1][L-1] + num[K-1][L+1]

import sys
inputData = int(sys.stdin.readline().strip())

#inputData = 100

num = [[0]*10 for x in range(101)]

for i in range(1, 10):
    num[1][i] = 1

for cnt in range(2, inputData+1):
    for check_num in range(10):
        if check_num == 0:
            num[cnt][check_num] = num[cnt - 1][check_num + 1]
        elif check_num == 9:
            num[cnt][check_num] = num[cnt - 1][check_num - 1]
        else:
            num[cnt][check_num] = num[cnt - 1][check_num - 1] + num[cnt - 1][check_num + 1]

print(sum(num[inputData])%1000000000)
