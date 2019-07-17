#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mini Fantasy War
# https://www.acmicpc.net/problem/12790

import sys
num = int(sys.stdin.readline().strip())

for cnt in range(num):
    power_list = str(sys.stdin.readline().strip()).split(' ')

    HP = 1 if (int(power_list[0]) + int(power_list[4])) < 1 else (int(power_list[0]) + int(power_list[4]))
    MP = 1 if (int(power_list[1]) + int(power_list[5])) < 1 else (int(power_list[1]) + int(power_list[5]))
    PO = 0 if (int(power_list[2]) + int(power_list[6])) < 0 else (int(power_list[2]) + int(power_list[6]))
    DE = int(power_list[3]) + int(power_list[7])

    power = 1 * (HP) + 5 * (MP) + 2 * (PO) + 2 * (DE)

    print(power)
