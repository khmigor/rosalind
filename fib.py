#!/usr/bin/env python
"""
Rabbits and Recurrence Relations
"""

def get_n_th(n, k, counter):
    if n in counter:
        return counter[n]
    return get_n_th(n - 1, k, counter) + k * get_n_th(n - 2, k, counter)


def main():
    with open('src')  as src, open('dst', 'w+') as dst:
        n, k = [int(x) for x in src.readline().strip().split()]
        counter = dict()
        counter[1] = counter[2] = 1
        n_th_count = get_n_th(n, k, counter)
        dst.write(str(n_th_count))


if __name__ == '__main__':
    main()