#!/usr/bin/env python
"""
Counting Point Mutations
"""

def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		first = src.readline().strip()
		second = src.readline().strip()
		diff = sum(int(f != s) for f, s in zip(first, second))
		dst.write(str(diff))

if __name__ == '__main__':
	main()