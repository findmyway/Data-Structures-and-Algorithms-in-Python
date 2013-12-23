#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   extend class progressions
#
#   Create time: 2013-12-22 15:11:46

from progressions import  Progression


class MinusProgression(Progression):
    """Minus the previous two number"""
    def __init__(self, first=2, second=200):
        """input two numbers"""
        super().__init__(first)
        self._second = second

    def _advance(self, ):
        self._current, self._second = self._second, abs(self._second - self._current)

if __name__ == '__main__':
    MinusProgression().print_progression(10)
