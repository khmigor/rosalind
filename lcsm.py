#!/usr/bin/env python
"""
Finding a Shared Motif
"""

def find_longest_common(first, second):
    matrix = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    best, score = '', 0
    for i, f in enumerate(first):
        for j, s in enumerate(second):
            if f == s:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
                if score < matrix[i + 1][j + 1]:
                    score = matrix[i + 1][j + 1]
                    best = first[i - score + 1 : i + 1]
    return best


def find_longest_common_in_list(strings):
    common = strings.pop()
    while strings:
        common = find_longest_common(strings.pop(), common)
    return common


def main():
    strings = list()
    with open('src')  as src:
        string = ''
        for line in src:
            if line.startswith('>'):
                if string:
                    strings.append(string)
                string = ''
            else:
                string += line.rstrip()
        if string:
            strings.append(string)

    common = find_longest_common_in_list(strings)
    with open('dst', 'w+') as dst:
        dst.write(common)
        

if __name__ == '__main__':
    main()