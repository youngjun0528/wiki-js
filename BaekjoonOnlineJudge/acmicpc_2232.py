#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 지뢰
# https://www.acmicpc.net/problem/2232

import sys
cnt = int(sys.stdin.readline().strip())
num = list()
for n in range(cnt):
    num.append(int(sys.stdin.readline().strip()))

result = list()
while True:
    if sum(num) == 0:
        break
    max_num = max(num)
    max_num_idx = num.index(max_num)
    num[max_num_idx] = 0
    num_sub = list()
    compare = max_num
    for i in range(max_num_idx-1, -1, -1):
        if 0 < num[i] < compare:
            num_sub.append(num[i])
            compare = num[i]
            num[i] = 0
        else:
            break
    compare = max_num
    for i in range(max_num_idx+1, len(num), +1):
        if 0 < num[i] < compare:
            num_sub.append(num[i])
            compare = num[i]
            num[i] = 0
        else:
            break
    result.append(max_num_idx+1)

for d in sorted(result):
    print(d)
