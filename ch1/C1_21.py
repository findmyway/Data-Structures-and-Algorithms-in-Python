#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 11:43:06

if __name__ == '__main__':
    try:
        while True:
            a = input("input an int:")
            print("%s" %(a))
    except EOFError:
        pass
