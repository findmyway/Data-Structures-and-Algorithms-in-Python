#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/17 9:01:47
if __name__ == '__main__':
    from itertools import permutations
    for x in permutations(reversed([1, 2, 3, 4, 5]), 3):
        print(x)
