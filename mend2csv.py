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

cli_help="""
Processes Mendeley bibliographic entries. Can also optionally export the loaded
file into a different format.
"""

## Use this to dump the keywords from the input file
def dump_bib_keywords (manager):
    keywords = manager.dump_keywords ()
    with open ('keywords.txt', 'w', encoding='utf8') as fp:
        for keyword in keywords:
            fp.write (keyword + '\n')

    print ('Dumped keywords to', os.path.abspath ('keywords.txt'))

def dump_bib_authors (manager):
    authors = manager.dump_authors ()
    with open ('authors.txt', 'w', encoding='utf8') as fp:
        for author in authors:
            fp.write (author + '\n')

    print ('Dumped author list to', os.path.abspath ('authors.txt'))

def main (args, input_file_path):
    # File I/O
    with open (input_file_path, 'r', encoding='utf8') as in_file:
        in_lines = in_file.readlines ()

    manager = BibManager ()
    manager.lines2entries (in_lines, data_type=args.input_format) # Load into ADT

    ## Process
    if args.dump_keywords:
        dump_bib_keywords (manager)

    if args.dump_authors:
        dump_bib_authors (manager)

    ## Save the file
    if args.save_file is not None:
        output_file_path = os.path.abspath (args.save_file)
        print ('Saving to', output_file_path)
        manager.entries2lines (data_type=args.output_format) # Export to desired DT
        out_lines = manager.lines
        with open (output_file_path, 'w', encoding='utf8') as out_file:
            for line in out_lines:
                out_file.write (line + '\n')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser (description=cli_help)
    parser.add_argument (dest='input_file', help='The file to load bib entries from. See README for implemented formats')
    # parser.add_argument (dest='output_file', help='The file to export bib entries to. If a file exists, it will be silently overwritten')

    input_format_group = parser.add_argument_group (title='Input formats')
    input_format_group.add_argument ('--input-format', dest='input_format', action='store', help='Input file format')
    input_format_group.add_argument ('--output-format', dest='output_format', action='store', help='Output file format')

    command_group = parser.add_argument_group (title='Commands')
    command_group.add_argument ('--dump-keywords', dest='dump_keywords', action='store_true', help='Dump the entry keywords to a file')
    command_group.add_argument ('--dump-authors', dest='dump_authors', action='store_true', help='Dump the entry authors to a file')
    command_group.add_argument ('--output-file', dest='save_file', action='store', help='The file to export bib entries to. If a file exists, it will be silently overwritten')

    args = parser.parse_args ()

    ## Check dependencies
    if args.save_file and not args.output_format:
        print ('You must specify an output format when saving a file. Aborting...')
        sys.exit ()

    ## Load the file
    input_file_path = os.path.abspath (args.input_file)
    if not os.path.exists (input_file_path) or os.path.isdir (input_file_path):
        print ('Input file doesn\'t exist or is a directory. Aborting...')
        sys.exit ()

    ## Arguments have been parsed. Now call the program
    main (args, input_file_path)