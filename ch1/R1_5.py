#!/usr/bin/env python3
# Author: TianJun
# Created Time: 2013/12/16 10:25:57

def sum_list(n):
    return sum([a * a for a in range(n)])

if __name__ == "__main__":
    print(sum_list(3))
