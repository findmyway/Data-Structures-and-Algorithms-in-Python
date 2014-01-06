#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#       if a stringsis a palindrome
#
#   Create time: 2013-12-28 20:39:18


def palindrome(s):
    if len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            return palindrome(s[1:-1])
    else:
        return True

if __name__ == '__main__':
    print(palindrome('racecar'))
    print(palindrome('gohangasalamiimalasagnahog'))
