#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 나머지 계산
# https://www.acmicpc.net/problem/3944

'''
5
10 7829
7 123456
6 432504023545112
8 37777777777777773
2 10110100010101010101101110001010001010101010101010111
'''

import sys

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")

num = int(sys.stdin.readline().rstrip())

# 모듈러 연산 결과
# X^n mod (X-1) == X mod (X-1) 와 동일하다
for n in range(num):
    cnt, check_num = sys.stdin.readline().rstrip().split()
    print(list(map(int, check_num)))
    rest = sum(list(map(int, check_num)))
    print(rest % (int(cnt) - 1))

# 일반 Python 진법 변환 후 나머지 연산 
for n in range(num):
    cnt, check_num = sys.stdin.readline().rstrip().split()
    answer = int(check_num, int(cnt))
    print(answer % (int(cnt) - 1))
