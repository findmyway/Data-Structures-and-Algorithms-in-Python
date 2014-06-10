#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 11:43:06

if __name__ == '__main__':
    s = []
    print("input anything you want, end with ctrl-d")
    try:
        while True:
            a = input()
            s.append(a)
    except EOFError:
        s.reverse()
        print("the reversed input are:")
        for x in s:
            print(x)
