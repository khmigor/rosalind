#!/usr/bin/env python
"""
RNA Splicing
"""

import re
from collections import defaultdict


def read_rna_codon_table(as_dna=False):
    acids = dict()
    with open('rna_codon') as rna_codon:
        for line in rna_codon:
            elements = line.strip().split()
            i = 0
            while i < len(elements):
                codon = elements[i]
                if as_dna:
                    codon = re.sub('U', 'T', codon)
                acids[codon] = elements[i + 1]
                i += 2
    return acids


def main():
    with open('src')  as src:
        dna = None
        introns = list()
        string = ''
        for line in src:
            if line.startswith('>'):
                if dna is not None:
                    introns.append(string)
                elif string:
                    dna = string
                string = ''
            else:
                string += line.rstrip()
        if string:
            introns.append(string)

    pattern = re.compile('|'.join(introns))
    exons = pattern.sub('', dna)
    acids_table = read_rna_codon_table(as_dna=True)
    acids = list()
    i = 0
    while i < len(exons):
        acids.append(acids_table[exons[i:i+3]])
        i += 3
    protein = ''.join((acid for acid in acids if acid != 'Stop'))
    with open('dst', 'w+') as dst:
        dst.write(protein)
        

if __name__ == '__main__':
    main()