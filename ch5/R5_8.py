#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R5_8.py
#       Description:
#           evalue pop of list
#
#       Last Modified:
#           2014-06-26 16:28:02

import time
L = 10 ** 6


def pop_test(N, position):
    A = [None] * L
    t0 = time.time()
    for i in range(N):
        A.pop(len(A) // 2 if position == 1 else position)
    return time.time() - t0


if __name__ == '__main__':
    print('\tN={}\tN={}\tN='.format('',
                                    str(10 ** 2),
                                    str(10 ** 3),
                                    str(10 ** 4),
                                    str(10 ** 5)))
    for p in [-1, 1, 0]:
        print('k = ', p, end='\t')
        for i in range(2, 6):
            N = 10 ** i
            print(pop_test(N, p), end='\t')
        print('')
