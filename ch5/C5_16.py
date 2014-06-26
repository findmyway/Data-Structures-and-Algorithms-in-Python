#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C5_16.py
#       Description:
#           update pop method of DynamicArray
#
#       Last Modified:
#           2014-06-26 19:33:46
from dynamic_array import DynamicArray


class MyArray(DynamicArray):
    def __init__(self):
        super().__init__()

    def pop(self):
        self._n -= 1
        if self._n <= 0:
            raise IndexError
        if self._n < self._capacity / 4:
            self._capacity = self._capacity // 2
        return self._A[self._n - 1]

    def __str__(self):
        a = []
        for i in range(self._n):
            a.append(self._A[i])
        return '[' + ','.join(str(x) for x in a) + ']'

if __name__ == '__main__':
    a = MyArray()
    for i in range(100):
        a.append(i)
    print(a)
    for i in range(100):
        x = a.pop()
        print("len:{},capacity:{}".format(a._n, a._capacity))
