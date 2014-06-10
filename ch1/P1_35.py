#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/17 9:26:15


def birthday_paradox():
    from random import randint
    from C1_15 import is_distinct
    for pepNum in range(5, 101, 5):
        #each case test 1000 times
        nTimes = 0
        for i in range(1000):
            birthdays = []
            for j in range(pepNum):
                birthdays.append(randint(1, 365))
            if not is_distinct(birthdays):
                nTimes += 1
        print("When n=%d, the probability is %.3f" % (pepNum, nTimes / 1000))


if __name__ == '__main__':
    birthday_paradox()
