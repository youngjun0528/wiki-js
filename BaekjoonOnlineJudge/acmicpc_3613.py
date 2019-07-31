#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Java vs C++
# https://www.acmicpc.net/problem/3613

'''
longAndMnemonic Identifier

longAndMnemonicIdentifieR_

_longAndMnemonicIdentifieR

longandmnemonicidentifier_
'''

import sys

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")

test = str(sys.stdin.readline().rstrip())

# C와 Java 변수명 차이
# 첫문자는 항상 소문자여야 한다.
# 마지막 문자는 '_' 로 끝나면 안된다.
# 문자열 중에 '_' 가 포함되어 있으면 C
# 문자열 중에 '_' 가 연속으로 있으면 안된다.
#

if test[0] == test[0].lower() and '_' != test[0] and '_' != test[-1]:
    if '_' in test:
        if '__' in test or ' ' in test:
            print('Error!')
        else:
            if test.islower():
                while True:
                    if '_' in test:
                        test = test.replace(str('_'+test[test.index('_')+1]), str(test[test.index('_')+1]).upper())
                    else:
                        break
                print(test)
            else:
                print('Error!')
    else:
        if '__' in test or ' ' in test:
            print('Error!')
        else:
            result = ''
            for c in test:
                if c.isupper():
                    result += '_' + c.lower()
                else:
                    result += c
            print(result)
else:
    print('Error!')




