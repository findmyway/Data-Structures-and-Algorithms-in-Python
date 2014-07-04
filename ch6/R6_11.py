#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R6_11.py
#       Description:
#           use collections.deque to inplement queue
#
#       Last Modified:
#           2014-06-27 10:48:50
from collections import deque


class MyQueue():
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        return self._data[0]

    def dequeue(self):
        self._data.popleft()

    def enqueue(self, v):
        self._data.append(v)
