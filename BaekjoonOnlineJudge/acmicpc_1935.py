#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 후위표기식2
# https://www.acmicpc.net/problem/1935

from string import ascii_uppercase

def main(operator, inputData):
    # ('ABC*+DE/-', ['1', '2', '3', '4', '5'])
    alpa = list(ascii_uppercase)
    testData = {}
    for cnt in range(len(inputData)):
       testData[alpa[cnt]] = int(inputData[cnt])
    # {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4}
    result = []
    for op in operator:
        if op == '/':
            a = result.pop()
            b = result.pop()
            if a in testData:
                a = testData[a]
            if b in testData:
                b = testData[b]
            result.append(float(b) / float(a))
        elif op == '*':
            a = result.pop()
            b = result.pop()
            if a in testData:
                a = testData[a]
            if b in testData:
                b = testData[b]
            result.append(b * a)
        elif op == '+':
            a = result.pop()
            b = result.pop()
            if a in testData:
                a = testData[a]
            if b in testData:
                b = testData[b]
            result.append(b + a)
        elif op == '-':
            a = result.pop()
            b = result.pop()
            if a in testData:
                a = testData[a]
            if b in testData:
                b = testData[b]
            result.append(b - a)
        else:
            result.append(op)
    print("%0.2f" % result[0])

import sys
if __name__ == '__main__':
    num = sys.stdin.readline().strip()
    operator = sys.stdin.readline().strip()
    inputData = []
    for cnt in range(int(num)):
        inputData.append(sys.stdin.readline().strip())
    main(operator, inputData)




