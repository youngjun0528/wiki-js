#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 골롱 수열
# https://www.acmicpc.net/problem/2038

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 
# 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5

# 분석
# 1
# 1

# 1, [2]
# 1, {[2], 2}

# 1, 2, [3]
# 1, 2, [2], {3, 3}

# 1, 2, 3, [4]
# 1, 2, 2, [3], 3, {4, 4, 4}

# 1, 2, 3, 4, [5]
# 1, 2, 2, 3, [3], 4, 4, 4, {5, 5, 5}

# 1, 2, 3, 4, 5, [6]
# 1, 2, 2, 3, 3, [4], 4, 4, 5, 5, 5, {6, 6, 6, 6}

import sys
num = int(sys.stdin.readline().strip())
sum = 0
mp = [0, 1]
sum += mp[1]

if num == 1:
    print(1)
else:
    for cnt in range(2, num):
        # 골롱 수열 점화식
        mp.append(1 + mp[cnt - mp[mp[cnt - 1]]])
        sum += mp[cnt]
        # sum에는 계속해서 골롱 수열의 f(i) 값이 담기고 있고 결국 sum이 n을 넘으면
        # 그때 i값이 n일때 f(n) 의 값이 된다.
        if sum >= num:
            break

    print(cnt)
