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
from mendproc.bibmanager import BibManager
from mendproc import Parsers

cli_help="""
Processes Mendeley bibliographic entries. Can also optionally export the loaded
file into a different format.
"""

## Use this to dump the keywords from the input file
def dump_bib_keywords (manager, output_dir_path):
    keywords = manager.dump_keywords (lowercase=True)

    if output_dir_path is not None:
        output_file_path = os.path.join (output_dir_path, 'keywords.txt')
    else:
        output_file_path = 'keywords.txt'

    with open (output_file_path, 'w', encoding='utf8') as fp:
        for keyword in keywords:
            fp.write (keyword + '\n')

    print ('Dumped keywords to', output_file_path)

def dump_bib_authors (manager):
    authors = manager.dump_authors ()

    if output_dir_path is not None:
        output_file_path = os.path.join (output_dir_path, 'authors.txt')
    else:
        output_file_path = 'authors.txt'

    with open (output_file_path, 'w', encoding='utf8') as fp:
        for author in authors:
            fp.write (author + '\n')

    print ('Dumped author list to', output_file_path)

def process_args (bibmanager, arguments, output_dir_path):
    if args.pattern is not '':
        bibmanager.cutoff_keywords_regex (args.pattern)

    if args.cutoff_year is not '':
        bibmanager.cutoff_year (int(args.cutoff_year))

    if args.dump_keywords:
        dump_bib_keywords (bibmanager, output_dir_path)

    if args.dump_authors:
        dump_bib_authors (bibmanager, output_dir_path)

    return (bibmanager)

def main (args, input_file_path):
    if args.output_dir:
        output_dir_path = os.path.abspath (args.output_dir)
        if not os.path.isdir (output_dir_path):
            os.mkdir (output_dir_path)
    else:
        output_dir_path = None

    # File I/O
    with open (input_file_path, 'r', encoding='utf8') as in_file:
        in_lines = in_file.readlines ()

    manager = BibManager ()
    manager.lines2entries (in_lines, data_type=args.input_format) # Load into ADT

    ## Process
    manager = process_args (manager, args, output_dir_path)

    ## Save the file
    if args.save_file is not None:
        if output_dir_path is not None:
            output_file_path = os.path.join (output_dir_path, args.save_file)
        else:
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

    input_format_group = parser.add_argument_group (title='Input formats')
    input_format_group.add_argument ('--input-format', dest='input_format', action='store', help='Input file format')
    input_format_group.add_argument ('--output-format', dest='output_format', action='store', help='Output file format')
    input_format_group.add_argument ('--output-dir', dest='output_dir', action='store', help='Output')

    command_group = parser.add_argument_group (title='Commands')
    command_group.add_argument ('--dump-keywords', dest='dump_keywords', action='store_true', help='Dump the entry keywords to a file')
    command_group.add_argument ('--dump-authors', dest='dump_authors', action='store_true', help='Dump the entry authors to a file')
    command_group.add_argument ('--output-file', dest='save_file', action='store', help='The file to export bib entries to. If a file exists, it will be silently overwritten')
    command_group.add_argument ('--cutoff-year', dest='cutoff_year', action='store', help='Ignore entries older than year specified')
    command_group.add_argument ('--keyword-regex', dest='pattern', action='store', help='Ignore entries that don\'t match')

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