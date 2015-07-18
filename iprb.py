#!/usr/bin/env python
"""
Mendel's First Law
"""

def main():
    with open('src')  as src, open('dst', 'w+') as dst:
        k, m, n = [float(x) for x in src.readline().strip().split()]
        probability = 1.0 - (m * (m - 1) / 4 + n * (m + n - 1)) / (m + n + k) / (m + n + k - 1)
        dst.write(str(probability))
        

if __name__ == '__main__':
    main()