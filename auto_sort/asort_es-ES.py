#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Christopher L
# Blog: http://blog.chriscabin.com
# GitHub: https://www.github.com/chrisleegit
# File: asort.py
# Date: 2016/08/22 11:12
# Version: 0.2
# Description: A python script to sort items alphabetically.

import os
import shutil
import re

README_FILE = '../README_es-ES.md'
TEMP_FILE = 'temp_es-ES.md'

# Only works for items between BEGIN and END.
BEGIN = '## Aplicaciones'
END = '## Configurar'

regex = re.compile(r"[^[]*\[([^]]*)\]")

def main():
    global README_FILE

    # Make sure the script can find the file: README.md
    README_FILE = os.path.abspath(README_FILE)

    if not os.path.exists(README_FILE):
        print(f'Error: archivo o directorio no existe: {README_FILE}')
        exit(1)

    sort_enable = False
    items = []

    print(f'Cargando archivo: {README_FILE}')

    # Read the file: README.md
    with open(README_FILE, 'r') as infile, open(TEMP_FILE, 'w') as outfile:
        # Process each line
        for line in infile:
            if not sort_enable and BEGIN in line:
                sort_enable = True

            if sort_enable and line.startswith('-'):
                line = line.strip()
                items.append(line)
            elif sort_enable and not line.startswith('-') and line == '\n':
                # When we meet the next header, we should stop adding new items to the list.
                for item in sorted(items, key=lambda x: regex.findall(x.upper())[-1]):
                    # Write the ordered list to the temporary file.
                    print(item, file=outfile)
                items.clear()

                # Remember to put the next header in the temporary file.
                print(line, end='', file=outfile)
            elif (
                sort_enable
                and not line.startswith('-')
                and line != '\n'
                and line.startswith('#')
            ):
                sort_enable = END not in line
                print(line, end='', file=outfile)
            else:
                print(line, end='', file=outfile)

    print('Reemplazar el archivo original: README_es-ES.md')
    shutil.move(TEMP_FILE, README_FILE)

if __name__ == '__main__':
    main()
