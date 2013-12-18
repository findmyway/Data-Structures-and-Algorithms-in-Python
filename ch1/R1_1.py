#!/usr/bin/env python3
def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    print(is_multiple(2, 3))
