#!/usr/bin/env python
"""
Calculating Expected Offspring
"""

def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		numbers = [float(x) for x in src.readline().strip().split()]
		number = 2 * (numbers[0] + numbers[1] + numbers[2]) + 1.5 * numbers[3] + numbers[4]
		dst.write(str(number))


if __name__ == '__main__':
	main()