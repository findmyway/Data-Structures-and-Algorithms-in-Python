#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   simulate the ecosystem of bears and fish
#   '-' means bears '|' means fish 'O' means None
#
#   Create time: 2013-12-22 16:23:08


import random as rd
RIVER_LENGTH = 100
#suggest the lenth is 100, initialize the river
river = str()
for i in range(RIVER_LENGTH):
    river += rd.choice("-|O")
print("""The river is:
      %s""" % (river))
print("There are {0} bears and {1} fishes".format
      (river.count('-'), river.count('|')))

# initialize the direction to move
# to simplify this question, we assume the river is a circle
# which means the head and tail are connected
# the value of directions means
# '-1':move to left; '0':stay, '1':move to right
directions = []
for i in range(RIVER_LENGTH):
    directions.append(rd.choice((-1, 0, 1)))
# Now move
n = 0
while True:
    for i in range(RIVER_LENGTH):
        if river[i] == 'O' or directions[i] == 0:
            pass
    n += 1
    print("Now after the %d round(s) move,the river is below".format(n))
