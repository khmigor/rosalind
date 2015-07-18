#!/usr/bin/env python
"""
Enumerating Gene Orders
"""

from itertools import permutations


def main():
    with open('src')  as src, open('dst', 'w+') as dst:
        number = int(src.readline().strip())
        perms = list(permutations((range(1, number + 1))))
        dst.write(str(len(perms)) + '\n')
        for perm in perms:
            dst.write(' '.join(str(n) for n in perm) + '\n')

            
if __name__ == '__main__':
    main()