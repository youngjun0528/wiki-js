#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 심부름 가는 길
# https://www.acmicpc.net/problem/5554

import sys
time_stamp = []
for cnt in range(4):
    num = int(sys.stdin.readline().strip())
    time_stamp.append(num)

hour = int(sum(time_stamp) / 60)

minute = sum(time_stamp) % 60

print(hour)
print(minute)
