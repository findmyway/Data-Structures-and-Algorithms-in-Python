#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   string reverse
#
#   Create time: 2013-12-28 20:04:26


def reverse_str(s):
    if len(s) >= 2:
        innerReversed = reverse_str(s[1:-1])
        innerReversed.append(s[0])
        innerReversed.insert(0, s[-1])
        return innerReversed
    else:
        return list(s)

if __name__ == '__main__':
    print(''.join(reverse_str('pots&pans')))
