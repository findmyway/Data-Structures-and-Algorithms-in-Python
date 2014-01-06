#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   find file in a given path
#
#   Create time: 2013-12-28 20:51:13
import os


def find_file(path, filename):
    for x in os.listdir(path):
        try:
            if os.path.isdir(path + os.sep + x):
                if find_file(path + os.sep + x, filename):
                    #如果该目录下找到了文件就返回True，否则继续查找
                    return True
            else:
                if x == filename:
                    return True
        except:
            #当遇到以 .开头的隐藏文件夹时回报错，忽略
            pass
    #如果遍历了所有文件和目录都没找到，则返回False
    return False

if __name__ == '__main__':
    path = os.path.abspath('..')
    print('If P4_23.py in parrent dir? {0}'
          .format(find_file(path, 'P4_23.py')))
    print('If P4_23.py in current dir? {0}'
          .format(find_file('.', 'P4_23.py')))
