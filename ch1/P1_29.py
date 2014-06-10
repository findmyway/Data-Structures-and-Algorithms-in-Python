#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/17 9:01:47
if __name__ == '__main__':
    from itertools import permutations
    s = 'catdog'
    for i in range(len(s)):
        for x in permutations(s, i + 1):
            print(''.join(x))
