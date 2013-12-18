#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 19:33:25
def rmPunctuation(string):
    returnString = str()
    for a in string:
        if a.isalpha() or a == ' ':
            returnString += a
    return returnString
if __name__ == '__main__':
    print(rmPunctuation("Lets try, Mike."))
