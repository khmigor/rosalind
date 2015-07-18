#!/usr/bin/env python
"""
Complementing a Strand of DNA
"""

from string import maketrans


COMPLEMENTATION_TABLE = maketrans('ACGT', 'TGCA')


def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		dna = src.readline()
		complement = dna.translate(COMPLEMENTATION_TABLE)
		reverse_complement = complement[::-1]
		dst.write(reverse_complement)
		

if __name__ == '__main__':
	main()