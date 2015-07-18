#!/usr/bin/env python
"""
Transcribing DNA into RNA 
"""

from string import maketrans


def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		dna = src.readline()
		rna = dna.replace('T', 'U')
		dst.write(rna)
		

if __name__ == '__main__':
	main()