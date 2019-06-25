#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 돌다리 건너기
# https://www.acmicpc.net/problem/2602

# inputData = 'RGS'
# A = 'RINGSR'
# B = 'GRGGNS'
#
# inputData = 'RRRRRRRRRR'
# A = 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'
# B = 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'
# #
inputData = 'RINGS'
A = 'SGNIRSGN'
B = 'GNIRSGNI'
# #
# inputData = 'GG'
# A = 'GGGGRRRR'
# B = 'IIIIGGGG'

check_arr = dict()

# https://docs.python.org/3/library/itertools.html#itertools.permutations
def permutations(iterable, r=None):
    global check_arr
    id = 0
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    var = [pool[i] for i in indices[:r]]
    if var not in check_arr.values():
        check_arr[id] = var
        id += 1
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                var = [pool[i] for i in indices[:r]]
                if var not in check_arr.values():
                    check_arr[id] = var
                    id += 1
                break
        else:
            return


data = [x for x in inputData.strip()]
data.extend([' ']*(len(A)-len(data)))
print(data)

permutations(data)

import itertools
# U = itertools.permutations(data)
# print(list(U))
# print(set(list(map(''.join, itertools.permutations(data)))))

C = [data[0]]
D = []
result = []
for cnt in range(1, len(data)):
    if cnt % 2 == 0:
        C.append(data[cnt])
    else:
        D.append(data[cnt])

print(C)
print(D)

print(check_arr.values())

for check in check_arr.values():
    target = ['0'] * len(A)
    for c in C:
        for k in range(len(A)):
            if c == A[k] == check[k]:
                target[k] = c
                break
            else:
                if target[k] == '0':
                    target[k] = '0'
    for d in D:
        for k in range(len(B)):
            if d == B[k] == check[k]:
                target[k] = d
                break
            else:
                if target[k] == '0':
                    target[k] = '0'

    import collections
    target_cnt = collections.Counter(target)
    target_cnt.pop('0')
    if sum(target_cnt.values()) == len(inputData):
        if str(''.join(target)).replace('0','') == inputData:
            print(target)
            if target not in result:
                result.append(target)


    target = ['0'] * len(A)
    for c in C:
        for k in range(len(B)):
            if c == B[k] == check[k]:
                target[k] = c
                break
            else:
                if target[k] == '0':
                    target[k] = '0'


    for d in D:
        for k in range(len(A)):
            if d == A[k] == check[k]:
                target[k] = d
                break
            else:
                if target[k] == '0':
                    target[k] = '0'
    target_cnt = collections.Counter(target)
    target_cnt.pop('0')
    if sum(target_cnt.values()) == len(inputData):
        if str(''.join(target)).replace('0', '') == inputData:
            print(target)
            if target not in result:
                result.append(target)
print(result)
print(len(result))
