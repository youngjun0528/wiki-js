#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 알파벳 개수
# https://www.acmicpc.net/problem/10808

from string import ascii_lowercase
from collections import Counter

def main(inputData):
    alpa = list(ascii_lowercase)
    test = Counter(inputData)
    result = {}
    for a in alpa:
        result[a] = test[a]
    text = ''
    for b in sorted(result.items()):
        text = text + ' ' + str(b[1])
    print(text.lstrip())

import sys
if __name__ == '__main__':
    inputData = sys.stdin.readline().strip()
    main(inputData)
