#!/usr/bin/env python
"""
Translating RNA into Protein
"""

def read_rna_codon_table():
    acids = dict()
    with open('rna_codon') as rna_codon:
        for line in rna_codon:
            elements = line.strip().split()
            i = 0
            while i < len(elements):
                acids[elements[i]] = elements[i + 1]
                i += 2
    return acids


def main():
    acids_table = read_rna_codon_table()
    with open('src')  as src, open('dst', 'w+') as dst:
        rna = src.readline().strip()
        i = 0
        acids = list()
        while i < len(rna):
            acids.append(acids_table[rna[i:i+3]])
            i += 3
        protein = ''.join((acid for acid in acids if acid != 'Stop'))
        dst.write(protein)
        

if __name__ == '__main__':
    main()