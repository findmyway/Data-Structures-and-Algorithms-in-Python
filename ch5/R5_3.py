#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#
#
#   Create time: 2014-01-06 19:59:55

import sys
data = []
cur = 0
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    print('length:{0:3d};size in bytes:{1:4d}'.format(a, b))
    data.append(None)
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    print('length:{0:3d};size in bytes:{1:4d}'.format(a, b))
    data.pop()
