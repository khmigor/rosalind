#!/usr/bin/env python
"""
Overlap Graphs
"""

from collections import defaultdict


K = 3


def main():
    with open('src')  as src:
        name = None
        strings = defaultdict(str)
        for line in src:
            if line.startswith('>'):
                name = line[1:].rstrip()
            else:
                strings[name] += line.rstrip()

    ins = defaultdict(set)
    outs = defaultdict(set)

    for name, string in strings.iteritems(): 
        start = tuple(string[:3])
        finish = tuple(string[-3:])
        ins[start].add(name)
        outs[finish].add(name)

    with open('dst', 'w+') as dst:
        for glue in outs:
            for start_name in outs[glue]:
                for finish_name in ins[glue]:
                    if start_name != finish_name:
                        dst.write(start_name + ' ' + finish_name + '\n')


if __name__ == '__main__':
    main()