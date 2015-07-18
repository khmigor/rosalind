#!/usr/bin/env python
"""
Open Reading Frames
"""

from string import maketrans
from collections import defaultdict

COMPLEMENTATION_TABLE = maketrans('ACGU', 'UGCA')
STOP = '$'


def read_rna_codon_table():
	acids = dict()
	with open('rna_codon') as rna_codon:
		for line in rna_codon:
			elements = line.strip().split()
			i = 0
			while i < len(elements):
				acid = elements[i + 1]
				if elements[i + 1] == 'Stop':
					acid = STOP
				acids[elements[i]] = acid
				i += 2
	return acids


def get_possibles(rna, acids_table):
	found_possibles = set()
	possibles = defaultdict(str)
	for i in range(len(rna) - 2):
		type_ = str(i % 3)
		codon = rna[i:i+3]
		acid = acids_table[codon]	
		if (type_ in possibles and possibles[type_][-1] != STOP) or (type_ not in possibles and acid == 'M'):
			possibles[type_] += acid
			if acid == STOP:
				found_possibles.add(possibles[type_])
				possibles.pop(type_)

	"""
	unstopped = list()
	for type_ in possibles:
		if possibles[type_][-1] != STOP:
			unstopped.append(type_)
	for type_ in unstopped:
		possibles.pop(type_)
	"""

	all_possibles = list()
	for possible in found_possibles:
		parts = possible.lstrip('M').split('M')
		for i in range(len(parts)):
			all_possibles.append('M' + 'M'.join(parts[i:]))
	return all_possibles


def main():
	acids_table = read_rna_codon_table()
	with open('src')  as src, open('dst', 'w+') as dst:
		dna = ''
		for line in src:
			if not line.startswith('>'):
				dna += line.strip()

		rna = dna.replace('T', 'U')
		complement_rna = rna.translate(COMPLEMENTATION_TABLE)
		reverse_complement_rna = complement_rna[::-1]
		
		possibles = set(get_possibles(rna, acids_table) + get_possibles(reverse_complement_rna, acids_table))
		for possible in possibles:
			dst.write(possible[:-1] + '\n')



if __name__ == '__main__':
	main()