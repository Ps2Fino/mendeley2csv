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

## Use this to dump the keywords from the input file
def dump_bib_keywords (manager):
    keywords = []
    for entry in manager.entries:
        keyword_list = entry['keywords'].split (';')
        for keyword in keyword_list:
            keywords.append (keyword)

    with open ('keywords.txt', 'w') as fp:
        for keyword in keywords:
            fp.write (keyword + '\n')

def dump_bib_authors (manager):
    keywords = []
    for entry in manager.entries:
        keyword_list = entry['author'].split (';')
        for keyword in keyword_list:
            keywords.append (keyword)

    with open ('authors.txt', 'w') as fp:
        for keyword in keywords:
            fp.write (keyword + '\n')

def main (args, input_file_path, output_file_path):
    # File I/O
    with open (input_file_path, 'r', encoding='utf8') as in_file:
        in_lines = in_file.readlines ()

    manager = BibManager ()
    manager.lines2entries (in_lines, data_type=args.input_format) # Load into ADT

    ## Process
    if args.dump_keywords:
        dump_bib_keywords (manager)

    ## Save the file
    manager.entries2lines (data_type=args.output_format) # Export to desired DT
    out_lines = manager.lines
    with open (output_file_path, 'w', encoding='utf8') as out_file:
        for line in out_lines:
            out_file.write (line + '\n')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser (description='Processes Mendeley bibliographic entries')
    parser.add_argument (dest='input_file', help='The file to load bib entries from. See README for implemented formats')
    parser.add_argument (dest='output_file', help='The file to export bib entries to. If a file exists, it will be silently overwritten')

    parser.add_argument ('--input-format', dest='input_format', action='store', help='Input file format')
    parser.add_argument ('--output-format', dest='output_format', action='store', help='Output file format')

    command_group = parser.add_mutually_exclusive_group (required=False)
    command_group.add_argument ('--dump-keywords', dest='dump_keywords', action='store_true', help='Dump the entry keywords to a file')
    command_group.add_argument ('--dump-authors', dest='dump_authors', action='store_true', help='Dump the entry authors to a file')

    args = parser.parse_args ()

    ## Load the file
    input_file_path = os.path.abspath (args.input_file)
    output_file_path = os.path.abspath (args.output_file)
    if not os.path.exists (input_file_path) or os.path.isdir (input_file_path):
        print ('Input file doesn\'t exist or is a directory. Aborting...')
        sys.exit ()

    ## Arguments have been parsed. Now call the program
    main (args, input_file_path, output_file_path)