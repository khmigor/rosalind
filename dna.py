#!/usr/bin/env python
"""
Counting DNA Nucleotides
"""

from collections import Counter


def main():
    with open('src')  as src:
        dna = src.readline()
        counts = Counter(dna)

        for base in ('A', 'C', 'G', 'T'):
            print  counts[base], 


if __name__ == '__main__':
    main()