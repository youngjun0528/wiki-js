#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

import sys
num = int(sys.stdin.readline().strip())

import collections
cnt = 0
for i in range(num):
    str_check = str(sys.stdin.readline().strip())
    str_counter = list(filter(lambda x : x[1] > 1, collections.Counter(str_check).items()))
    if len(str_counter) > 0:
        test = True
        for str_for in str_counter:
            targt_str = [i for i, x in enumerate(str_check) if x == str_for[0]]
            test_str = list(range(targt_str[0], targt_str[0]+len(targt_str)))
            if targt_str != test_str:
                test = False
        if test:
            cnt += 1
    else:
        cnt += 1

print(cnt)


