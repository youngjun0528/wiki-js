#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 듣보잡
# https://www.acmicpc.net/problem/1764

import sys
line = str(sys.stdin.readline().strip()).split(' ')
duddo_cnt = int(line[0])
bodo_cnt = int(line[1])

duddo_list = list()
bodo_list = list()

for i in range(duddo_cnt):
    duddo_list.append(str(sys.stdin.readline().strip()))

for i in range(bodo_cnt):
    bodo_list.append(str(sys.stdin.readline().strip()))

dudbo_list = sorted(list(set(duddo_list) & set(bodo_list)))

print(len(dudbo_list))
for dudbo in dudbo_list:
    print(dudbo)
