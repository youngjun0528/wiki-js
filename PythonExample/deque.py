import time
timstamp1 = time.time()
print(timstamp1)
players = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

import collections
deq = collections.deque(players)
cnt = 0
while True:
    if len(deq) == 1:
        break
    a = deq.popleft()
    b = deq.popleft()
    if a > b:
        cnt = cnt + 1
        deq.append(a)
    elif a < b:
        cnt = cnt + 1
        deq.append(b)
    elif a == b and a == 1:
        cnt = cnt + 1
        deq.append(a)
    elif a == b and a == 0:
        deq.append(a)
    print(deq)
print(cnt)
timstamp2 = time.time()
print(timstamp2)
print(timstamp2 - timstamp1)

