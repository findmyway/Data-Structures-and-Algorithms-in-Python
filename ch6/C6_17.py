#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C6_16.py
#       Description:
#           change the implementation of arraystack
#
#       Last Modified:
#           2014-07-04 12:46:09


from array_stack import ArrayStack


class Full(Exception):
    pass


class MyStack(ArrayStack):
    def __init__(self, maxlen=None):
        super().__init__()
        self._maxlen = maxlen

    def push(self, e):
        """Add element e to the top of the stack."""
        if self.__len__() >= self._maxlen:  # Careful, when maxlen is None,
                                         # this comparision will raise an error
            raise Full("Stack is full!!!")
        self._data.append(e)                  # new item stored at end of list


if __name__ == '__main__':
    S = MyStack(5)
    for i in range(10):
        try:
            S.push(i)
        except Exception as e:
            print(e)
