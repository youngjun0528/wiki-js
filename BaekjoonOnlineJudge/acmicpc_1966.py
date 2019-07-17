#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mini Fantasy War
# https://www.acmicpc.net/problem/12790

'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

1
4 2
1 2 3 4

1
6 0
1 1 9 1 1 1
'''

import sys
import queue
num = int(sys.stdin.readline().strip())

for cnt in range(num):
    doc_check = str(sys.stdin.readline().strip()).split(' ')
    doc = int(doc_check[0])
    check = int(doc_check[1])

    print_doc_list = [int(x) for x in str(sys.stdin.readline().strip()).split(' ')]

    q = queue.Queue()
    for i in range(len(print_doc_list)):
        q.put((i, print_doc_list[i]))

    cnt = 0
    while True:
        print_doc_max = max([x[1] for x in list(q.queue)])
        #print(list(q.queue))
        if q.empty():
            break
        a = q.get()
        cnt += 1
        if a[1] < print_doc_max:
            q.put(a)
            cnt -= 1
        else:
            max_print_doc = print_doc_max
            if a[0] == check:
                break
    print(cnt)
