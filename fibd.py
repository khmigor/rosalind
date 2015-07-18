#!/usr/bin/env python
"""
Mortal Fibonacci Rabbits
"""

def main():
	with open('src')  as src, open('dst', 'w+') as dst:
		n, m = [int(x) for x in src.readline().strip().split()]
		born = {1: 1}
		for k in range(2, n + 1):
			born[k] = sum(born[k] for k in range(max(1, k - m), k - 1))
		answer = sum(born[k] for k in range(n - m + 1, n + 1))
		dst.write(str(answer))
		print born


if __name__ == '__main__':
	main()