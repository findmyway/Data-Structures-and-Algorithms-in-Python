#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 11:12:02
def is_distinct(dataList):
    lenList = len(dataList)
    setList = len(set(dataList))
    if lenList == setList:
        return True
    else:
        return False
if __name__ == '__main__':
    print(is_distinct([1, 2, 3, 3]))
    print(is_distinct([1, 2, 3]))
