#!/usr/bin/python
# -*- coding=utf-8 -*-

# 음계
# https://www.acmicpc.net/problem/2920

def main(inputData):
    asc = sorted(inputData, reverse=False)
    desc = sorted(inputData, reverse=True)
    if inputData == asc:
        print('ascending')
    elif inputData == desc:
        print('descending')
    else:
        print('mixed')

import sys
if __name__ == '__main__':
    inputData = sys.stdin.readline().strip().split(' ')
    main(inputData)
