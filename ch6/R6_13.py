#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R6_13.py
#       Description:
#           use queue to change [1,2,3,4,5,6,7,8] into
#           [1,2,3,5,4,6,7,8]
#       Last Modified:
#           2014-06-27 11:08:05


from array_queue import ArrayQueue

if __name__ == '__main__':
    D = ArrayQueue()
    Q = ArrayQueue()
    #initial D
    for i in range(1, 9):
        D.enqueue(i)

    D.enqueue(D.dequeue())
    D.enqueue(D.dequeue())
    D.enqueue(D.dequeue())  # D = [4,5,6,7,8,1,2,3]

    Q.enqueue(D.dequeue())  # Q = [4], D = [5,6,7,8,1,2,3]
    D.enqueue(D.dequeue())  # Q = [4], D = [6,7,8,1,2,3,5]
    D.enqueue(Q.dequeue())  # Q = [], D = [6,7,8,1,2,3,5,4]

    D.enqueue(D.dequeue())
    D.enqueue(D.dequeue())
    D.enqueue(D.dequeue())  # D = [1,2,3,5,4,6,7,8]

    for i in range(8):
        print(D.dequeue(), end=',')
