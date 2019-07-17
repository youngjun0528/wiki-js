#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
'''

import sys
import queue

open_check = ['(', '[']
close_check = [')', ']']

while True:
    org_str = str(sys.stdin.readline()).rstrip()
    if org_str == '.':
        break
    check_list = []

    for check_str in org_str:
        if check_str in open_check:
            check_list.append(check_str)
        if check_str in close_check:
            if len(check_list) > 0 and open_check[close_check.index(check_str)] == check_list[-1]:
                check_list.pop()
            else:
                check_list.append(check_str)
    if len(check_list) == 0:
        print("yes")
    else:
        print("no")



