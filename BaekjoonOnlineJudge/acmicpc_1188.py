#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 음식 평론가
# https://www.acmicpc.net/problem/1188

import sys
line = str(sys.stdin.readline().strip()).split(' ')
sosage = int(line[0])
man = int(line[1])

# sosage = 2 / man = 6 : 2/6(1/3) 조각 : 총 4번의 칼질 (2,6) 최대공약수 2 6-2
# sosage = 3 / man = 4 : 3/4      조각 : 총 3번의 칼질 (3,4) 최대공약수 1 4-1
# sosage = 6 / man = 6 : 1        조각 : 총 0번의 칼질 (6,6) 최대공약수 6 6-6
# sosage = 5 / man = 4 : 5/4      조각 : 총 3번의 칼질 (5,4) 최대공약수 1 4-1

def gcd( a, b):
    gcm = 1

    for k in range(2, min(a , b) + 1):
        while ( a % k == 0 ) & ( b % k == 0):
            a = a // k
            b = b // k
            gcm = gcm * k
            continue
    return gcm

print(man - gcd(man, sosage))
