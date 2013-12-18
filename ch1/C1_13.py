#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 11:00:31
def myRevers(data):
    for i in range(len(data) // 2):
        data[i], data[-i - 1] = data[-i - 1], data[i]
    return data
if __name__ == '__main__':
    print(myRevers([1, 2, 3, 4, 5]))
