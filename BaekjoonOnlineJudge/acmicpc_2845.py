#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 파티가 끝나고 난 뒤
# https://www.acmicpc.net/problem/2845

import sys

if __name__ == '__main__':
    num_arr = sys.stdin.readline().strip().split(' ')
    inputData_arr = sys.stdin.readline().strip().split(' ')
    member = int(num_arr[0]) * int(num_arr[1])
    result = ''
    for data in inputData_arr:
        result += str(int(data) - member) + ' '
    print(result)

    
