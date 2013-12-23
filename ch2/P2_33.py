#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   输入一个多项式的系数，阶数由高到低
#   输出其一阶导
#
#   Create time: 2013-12-22 15:35:15


def first_polynomial(polynomial):
    result = []
    try:
        lenth = len(polynomial)
        for k in reversed(range(lenth)):
            if not isinstance(polynomial[lenth-k-1], (int, float)):
                raise ValueError
            result.append(k * polynomial[lenth-k-1])
        return result
    except:
        print("Check input ! ValueError!")
        return False

if __name__ == '__main__':
    print(first_polynomial([3, 2, 1]))
    print(first_polynomial("fdfe"))
