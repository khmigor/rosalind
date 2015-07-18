#!/usr/bin/env python
"""
Calculating Protein Mass
"""

def read_table():
	masses = dict()
	with open('protein_mass') as src:
		for line in src:
			acid, mass = line.strip().split()
			masses[acid] = float(mass)
	return masses


def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		masses = read_table()
		string = src.readline().strip()
		total = sum(masses[acid] for acid in string)
		dst.write(str(total))


if __name__ == '__main__':
	main()