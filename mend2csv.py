##
## Extracts information of interest from
## Mendeley exported bib files
##
## Note this program expects input csv files
## to be complete with a header.
## Execuution is subject to unknowns without...
##
## @author Daniel J. Finnegan
## @date February 2019

import argparse
import os
import sys
from packages.bibmanager import BibManager
from packages import Parsers

def main (input_file_path, output_file_path, file_type):
    # File I/O
    with open (input_file_path, 'r', encoding='utf8') as in_file:
        in_lines = in_file.readlines ()

    manager = BibManager ()

    if file_type is 'b':
        manager.lines2entries (in_lines, data_type='csv')
        manger.entries2lines (data_type='bibtex')

    else:
        manager.lines2entries (in_lines, data_type='bibtex')
        manager.entries2lines (data_type='csv')

    ## File I/O
    out_lines = manager.lines
    with open (output_file_path, 'w', encoding='utf8') as out_file:
        for line in out_lines:
            out_file.write (line + '\n')

    if file_type is 'b':
        print ('Converted csv file to bib!')
    else:
        print ('Converted bib file to csv!')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser (description='Converts a bib file to a csv spreadsheet')
    parser.add_argument (dest='input_file', help='The bib or csv file to convert')
    parser.add_argument (dest='output_file', help='The bib or csv file to output. If a file exists, it will be silently overwritten')
    group = parser.add_mutually_exclusive_group (required=True)
    group.add_argument ('-b', '--to-bib', dest='to_bib', action='store_true', help='Convert a csv file to a bib file')
    group.add_argument ('-c', '--to-csv', dest='to_csv', action='store_true', help='Convert a bib file to a csv file')

    args = parser.parse_args ()

    ## Load the file
    input_file_path = os.path.abspath (args.input_file)
    output_file_path = os.path.abspath (args.output_file)
    if not os.path.exists (input_file_path) or os.path.isdir (input_file_path):
        print ('Input file doesn\'t exist or is a directory. Aborting...')
        sys.exit ()

    file_type = 'b' if args.to_bib else 'c'

    ## Arguments have been parsed. Now call the program
    main (input_file_path, output_file_path, file_type)