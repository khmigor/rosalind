#!/usr/bin/env python
"""
Finding a Protein Motif
"""

import re
import urllib2

regex = re.compile('(?=N[^P][ST][^P])')
url_format = 'http://www.uniprot.org/uniprot/{0}.fasta'

def main():
    string = ''
    with open('src')  as src, open('dst', 'w+') as dst:
        for line in src:
            incides = None
            name = line.strip()
            data = urllib2.urlopen(url_format.format(name)).read()
            string = ''.join(data.split('\n')[1:])
            indices = [m.start() + 1 for m in regex.finditer(string)]
            
            if indices:
                dst.write(name + '\n')
                dst.write(' '.join(str(index) for index in indices) + '\n')

            
if __name__ == '__main__':
    main()