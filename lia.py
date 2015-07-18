#!/usr/bin/env python
"""
Independent Alleles
"""

def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		k, n = [int(x) for x in src.readline().strip().split()]
		t = 2 ** k

		total = 0
		current = 1.0 / 4 ** t
		for i in range(t - 1, n - 2, -1):
			total += current
			current = current * 3 * (float(i + 1)) / (t - i)
		dst.write(str(total))


if __name__ == '__main__':
	main()