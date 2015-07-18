#!/usr/bin/env python
"""
Inferring mRNA from Protein
"""

from collections import Counter

MOD = 1000000


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
	counts = Counter()
	for codon, acid in acids_table.iteritems():
		counts[acid] += 1

	with open('src')  as src, open('dst', 'w+') as dst:
		protein = src.readline().strip()
		product = 1
		for acid in protein:
			product *= counts[acid]
			product %= MOD
		product *= 3
		dst.write(str(product))

if __name__ == '__main__':
	main()