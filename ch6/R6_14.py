#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R6_14.py
#       Description:
#           use deque to change [1,2,3,4,5,6,7,8] to
#           [1,2,3,5,4,6,7,8]
#
#       Last Modified:
#           2014-06-27 11:24:51


from collections import deque

if __name__ == '__main__':
    D = deque()
    S = deque()
    D.extend(i for i in range(1, 9))
    print(D)

    S.append(D.popleft())
    S.append(D.popleft())
    S.append(D.popleft())
    S.append(D.popleft())
    D.append(D.popleft())
    D.appendleft(S.pop())
    D.appendleft(D.pop())
    D.appendleft(S.pop())
    D.appendleft(S.pop())
    D.appendleft(S.pop())

    print(D)
