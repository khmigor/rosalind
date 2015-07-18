#!/usr/bin/env python
"""
Finding a Motif in DNA
"""

import re


def main():
    with open('src')  as src, open('dst', 'w+') as dst:
        dna = src.readline().strip()
        motif = src.readline().strip()
        indices = (m.start() + 1 for m in re.finditer('(?=' + motif + ')', dna))
        dst.write(' '.join(str(index) for index in indices))


if __name__ == '__main__':
    main()