#!/usr/bin/env python
"""
Consensus and Profile
"""

from collections import defaultdict


def main():
	with open('src')  as src:
		strings = defaultdict(str)
		for line in src:	
			if line.startswith('>'):
				name = line[1:].rstrip()
			else:
				strings[name] += line.rstrip()

	occurencies = None
	length = 0
	for string in strings.values():
		if occurencies is None:
			length = len(string) 
			occurencies = defaultdict(lambda: [0] * length)
		for index, symbol in enumerate(string):
			occurencies[symbol][index] += 1

	max_symbols = [None] * length
	for index in range(length):
		max_count = 0
		for symbol in occurencies:
			if max_count < occurencies[symbol][index]:
				max_count = occurencies[symbol][index]
				max_symbols[index] = symbol

	with open('dst', 'w+') as dst:
		dst.write(''.join(max_symbols) + '\n')
		for symbol in ('A', 'C', 'G', 'T'):
			dst.write(symbol + ': ' + ' '.join(str(s) for s in occurencies[symbol]) + '\n')


if __name__ == '__main__':
	main()