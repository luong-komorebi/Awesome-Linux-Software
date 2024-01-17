#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Christopher L
# Blog: http://blog.chriscabin.com
# GitHub: https://www.github.com/chrisleegit
# File: asort.py
# Date: 2024/01/15 15:30
# Version: 3.1
# Description: A versatile Python script for sorting items alphabetically in Markdown files.

from __future__ import print_function
import os
import shutil

README_FILE = '../README_en-US.md'
TEMP_FILE = 'temp_en-US.md'

# Only works for items between BEGIN and END.
BEGIN = '## Applications'
END = '## Configuration'

def main():
    global README_FILE

    # Ensure the script can find the file: README.md
    README_FILE = os.path.abspath(README_FILE)

    if not os.path.exists(README_FILE):
        print(f'Error: File or directory does not exist: {README_FILE}')
        exit(1)

    sorting_enabled = False
    items = []

    print(f'Loading file: {README_FILE}')

    # Read the file: README.md
    with (open(README_FILE) as infile, open(TEMP_FILE, 'w') as outfile):
        # Process each line
        for line in infile:
            if not sorting_enabled and BEGIN in line:
                sorting_enabled = True

            if sorting_enabled:
                line = line.strip()

                # Each item starts with a character '-' (maybe '*' and '+')
                if line.startswith(('-', '*', '+')):
                    items.append(line)
                elif line.startswith('#'):
                    sorting_enabled = END not in line

                    # When we meet the next header, stop adding new items to the list.
                    for item in sorted(items, key=lambda x: x.upper()):
                        # Write the ordered list to the temporary file.
                        print(item, file=outfile)
                    print('', file=outfile)
                    items.clear()

                    # Remember to put the next header in the temporary file.
                    print(line, file=outfile)
                else:
                    print(line, end='', file=outfile)
            else:
                print(line, end='', file=outfile)

    print('Replace the original file: README_en-US.md')
    shutil.move(TEMP_FILE, README_FILE)

if __name__ == '__main__':
    main()
