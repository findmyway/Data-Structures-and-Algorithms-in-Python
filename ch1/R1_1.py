#!/usr/bin/env python3


def is_multiple(n, m):
    return n % m == 0

if __name__ == "__main__":
    a, b = input("input 2 int, seperate with blank : ").split()
    print("is multiple ? ", is_multiple(int(a), int(b)))
