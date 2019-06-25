#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 가로수
# https://www.acmicpc.net/problem/2485

# 각 가로수 사이의 거리 중에서 최대 공약수를 구하여 처리한다.
import sys

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

if __name__ == '__main__':
    num = int(sys.stdin.readline().strip())
    inputData = []
    for cnt in range(num):
        inputData.append(int(sys.stdin.readline().strip()))

    #print(inputData)

    g = inputData[1] - inputData[0]
    for i in range(2, num):
        g = gcd(g, inputData[i] - inputData[i - 1])
    answer = (inputData[num - 1] - inputData[0]) // g + 1 - num
    print(answer)
