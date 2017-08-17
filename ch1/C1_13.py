#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 11:00:31
def myRevers(data):
    return [data[-(i+1)] for i in range(len(data))]
    
if __name__ == '__main__':
    print(myRevers([1, 2, 3, 4, 5]))
