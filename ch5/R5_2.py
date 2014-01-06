#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#
#
#   Create time: 2014-01-06 19:54:50

import sys
data = []
cur = 0
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    if b > cur and a > 0:
        cur = b
        print('Exausted when leng:w
              th = {0}'.format(a - 1))
    data.append(None)
