#!/usr/bin/env python
"""
Computing GC Content
"""

from collections import defaultdict


def compute_gc(string):
    return float(len(string.translate(None, 'AT'))) / len(string)

def main():
    with open('src')  as src:
        name = None
        strings = defaultdict(str)
        for line in src:
            if line.startswith('>'):
                name = line[1:].rstrip()
            else:
                strings[name] += line.rstrip()

    max_gc = 0 
    fittest_name = None

    for name, string in strings.iteritems(): 
        gc = compute_gc(string)
        if gc > max_gc:
            max_gc = gc
            fittest_name = name

    with open('dst', 'w+') as dst:
        dst.write(fittest_name + '\n' + str(100 * max_gc))


if __name__ == '__main__':
    main()