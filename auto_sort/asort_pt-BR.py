#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher L
# Blog   : http://blog.chriscabin.com
# GitHub : https://www.github.com/chrisleegit
# File   : asort.py
# Date   : 2016/08/22 11:12
# Version: 0.1
# Description: A very simple python script that can sort items alphabetically.

from __future__ import print_function
import os
import shutil


README_FILE = '../README_pt-BR.md'
TEMP_FILE = 'temp_pt-BR.md'

# only works for those items between BEGIN and END.
BEGIN = '## Aplicativos'
END = '## Configuração'


def main():
    global README_FILE

    # make sure the script can find file: README.md
    README_FILE = os.path.abspath(README_FILE)

    if not os.path.exists(README_FILE):
        print('Erro: Arquivo ou diretório não existe: {}'.format(README_FILE))
        exit(1)

    sort_enable = False
    items = list()

    print('Carregando arquivo: {}'.format(README_FILE))

    # read file: README.md
    with open(README_FILE) as infile, open(TEMP_FILE, 'w') as outfile:
        # process each line
        for line in infile:
            if not sort_enable and BEGIN in line:
                sort_enable = True

            # if sort_enable and END in line:
            #     sort_enable = False

            if sort_enable:
                line = line.strip()

                # each item starts with a character '-' (maybe '*' and '+')
                if line.startswith(('-', '*', '+')):
                    items.append(line)
                elif line.startswith('#'):
                    sort_enable = False if END in line else True

                    # when we meet the next header, we should stop adding new item to the list.
                    for item in sorted(items, key=lambda x: x.upper()):
                        # write the ordered list to the temporary file.
                        print(item, file=outfile)
                    print('', file=outfile)
                    items.clear()

                    # remember to put the next header in the temporary file.
                    print(line, file=outfile)
                else:
                    print(line, end='', file=outfile)
            else:
                print(line, end='', file=outfile)

    print('Substitua o arquivo original: README_pt-BR.md')
    shutil.move(TEMP_FILE, README_FILE)


if __name__ == '__main__':
    main()
