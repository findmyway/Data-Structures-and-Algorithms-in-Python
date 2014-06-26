#!/usr/bin/env python
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R5_4.py
#       Description:
#           change getitem method
#
#       Last Modified:
#           2014-06-26 13:11:19


from dynamic_array import DynamicArray


class MyArray(DynamicArray):
    def __init__(self):
        super().__init__()

    def __getitem__(self, k):
        """Return element at index k."""
        if k < 0:
            k += self._n
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                              # retrieve from array

if __name__ == '__main__':
    a = MyArray()
    for i in range(5):
        a.append(i)
    for i in range(5):
        print(a[-i])
    #test exception
    print(a[-10])
