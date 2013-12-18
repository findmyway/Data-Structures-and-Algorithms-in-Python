#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 10:50:00
def myChoice(data):
    import random
    chosenIndex = random.randrange(len(data))
    return data[chosenIndex]

if __name__ == '__main__':
    print(myChoice([1, 2, 3, 4]))
