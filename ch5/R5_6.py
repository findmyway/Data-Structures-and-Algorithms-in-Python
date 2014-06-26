#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R5_6.py
#       Description:
#           change insert
#
#       Last Modified:
#           2014-06-26 13:35:25


from dynamic_array import DynamicArray


class MyArray(DynamicArray):
    def __init__(self):
        super().__init__()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                  # not enough room
            B = self._make_array(2 * self._capacity)   # so double capacity
            for j in range(self._n, k, -1):            # shift rightmost first
                B[j] = self._A[j - 1]
            B[k] = value                             # store newest element
            for j in range(0, k):
                B[j] = self._A[j]
            self._A = B
            self._n += 1
            self._capacity = 2 * self._capacity

        else:
            for j in range(self._n, k, -1):            # shift rightmost first
                self._A[j] = self._A[j - 1]

            self._A[k] = value                          # store newest element
            self._n += 1

    def __str__(self):
        a = []
        for i in range(self._n):
            a.append(self._A[i])
        return '[' + ','.join(str(x) for x in a) + ']'

if __name__ == '__main__':
    a = MyArray()
    for i in range(20):
        a.insert(0, i)
        print(a)
