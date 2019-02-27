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
import re
import csv

# GENERAL_REGEX_PATTERN = '{((?=[\w\d:])(.*))}'
GENERAL_REGEX_PATTERN = '{((?=[\w\d:{])(.+))}'
CITATION_KEY_PATTERN = '^@(.*){(\S+),'

## Note this is not an exhaustive list
## There are more; these are just the ones I care about
KEYWORDS_PATTERN = '^keywords'
ABSTRACT_PATTERN = '^abstract'
AUTHOR_PATTERN = '^author'
DOI_PATTERN = '^doi'
YEAR_PATTERN = '^year'
TITLE_PATTERN = '^title'
URL_PATTERN = '^url'

## Helper function for capturing the content
def match_pattern (pattern, line):
    match_obj = pattern.search (line)
    info = match_obj.group (1) if match_obj else '' ## we've matched a new entry. Log it

    ## We also remove {} if they are at the end and beginning of the string
    if info != '':
        if info.startswith ('{'):
            info = info[1:]

        if info.endswith ('}'):
            info = info[:-1]

    return (info)

## This function takes a Mendeley formatted bib file
## and transforms it into a dictionary
def bib2dict (lines):
    entries = []
    entry = {}

    general_pattern = re.compile (GENERAL_REGEX_PATTERN)
    citation_key_pattern = re.compile (CITATION_KEY_PATTERN)
    keywords_pattern = re.compile (KEYWORDS_PATTERN)
    abstract_pattern = re.compile (ABSTRACT_PATTERN)
    author_pattern = re.compile (AUTHOR_PATTERN)
    doi_pattern = re.compile (DOI_PATTERN)
    url_pattern = re.compile (URL_PATTERN)
    year_pattern = re.compile (YEAR_PATTERN)
    title_pattern = re.compile (TITLE_PATTERN)

    for line in lines:
        stripped_line = line.strip (' \n')
        # print (stripped_line)
        match_obj = citation_key_pattern.search (stripped_line)
        if match_obj:
            if entry != {}:
                entries.append (entry)
                entry = {}

            ## Otherwise we start filling in the next one
            entry_type = match_obj.group (1) if match_obj else 'unknown'
            citation_key = match_obj.group (2) if match_obj else 'unknown' ## we've matched a new entry. Log it

            ## Prefill the entry
            entry['bibkey'] = citation_key # Store the sentinel bibkey
            entry['type'] = entry_type
            entry['abstract'] = ''
            entry['keywords'] = ''
            entry['author'] = ''
            entry['doi'] = ''
            entry['url'] = ''
            entry['year'] = ''
            entry['title'] = ''

        else:
            ## Otherwise, we're currently in the midst of an entry.
            ## Grab the stuff we care about
            if keywords_pattern.search (stripped_line):
                keywords = match_pattern (general_pattern, stripped_line)
                entry['keywords'] = keywords

            elif abstract_pattern.search (stripped_line):
                abstract = match_pattern (general_pattern, stripped_line)
                entry['abstract'] = abstract

            elif author_pattern.search (stripped_line):
                author = match_pattern (general_pattern, stripped_line)
                entry['author'] = author

            elif doi_pattern.search (stripped_line):
                doi = match_pattern (general_pattern, stripped_line)
                entry['doi'] = doi

            elif url_pattern.search (stripped_line):
                url = match_pattern (general_pattern, stripped_line)
                entry['url'] = url

            elif year_pattern.search (stripped_line):
                year = match_pattern (general_pattern, stripped_line)
                entry['year'] = year

            elif title_pattern.search (stripped_line):
                title = match_pattern (general_pattern, stripped_line)
                entry['title'] = title

    ## Don't forget about the sentinel!
    entries.append (entry)

    return (entries)

## Convert a list of lines in csv format to a dictionary
def csv2dict (lines):
    entries = []
    entry = {}
    csvlines_reader = csv.DictReader (lines, delimiter=',', quotechar='"')
    for row in csvlines_reader:
        entries.append (row)

    return (entries)

## Inverse operation of bib2dict
def dict2bib (entries):
    lines = []
    for entry in entries:
        lines = lines + entry2bibstr (entry) # Concatenate the entries

    return lines

## Convert an entry into a list of strings
def entry2bibstr (entry):
    lines = []
    lines.append ('@' + entry['type'] + re.sub ('@bibkey@', entry['bibkey'], '{@bibkey@,'))
    lines.append (re.sub ('@author@', entry['author'], 'author = {@author@},'))
    lines.append (re.sub ('@title@', entry['title'], 'title = {@title@},'))
    lines.append (re.sub ('@keywords@', entry['keywords'], 'keywords = {@keywords@},'))
    lines.append (re.sub ('@abstract@', entry['abstract'], 'abstract = {@abstract@},'))
    lines.append (re.sub ('@year@', entry['year'], 'year = {@year@},'))
    lines.append (re.sub ('@doi@', entry['doi'], 'doi = {@doi@},'))
    lines.append (re.sub ('@url@', entry['url'], 'url = {@url@},'))
    lines.append ('}')

    return (lines)

## Inverse operation of csv2dict
def dict2csv (entries):
    lines = []
    header = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"".format('type',
    'bibkey',
    'author',
    'title',
    'keywords',
    'abstract',
    'year',
    'doi',
    'url'
    )
    lines.append (header)

    for entry in entries:
        lines.append (entry2csvstr (entry))

    return (lines)

## convert an entry into a csv string
def entry2csvstr (entry):
    csvstr = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"".format(entry['type'],
    entry['bibkey'],
    entry['author'],
    entry['title'],
    entry['keywords'],
    entry['abstract'],
    entry['year'],
    entry['doi'],
    entry['url'],
    )

    return (csvstr)

## Conversion to and from csv files and bib files is now
## a trivial conversion
def bib2csv (lines):
    entries = bib2dict (lines)
    lines = dict2csv (entries)

    return (lines)

def csv2bib (lines):
    entries = csv2dict (lines)
    lines = dict2bib (entries)

    return (lines)

def main (input_file_path, output_file_path, file_type):
    # File I/O
    with open (input_file_path, 'r', encoding='utf8') as in_file:
        in_lines = in_file.readlines ()

    if file_type is 'b':
        out_lines = csv2bib (in_lines)
    else:
        out_lines = bib2csv (in_lines)

    ## File I/O
    with open (output_file_path, 'w', encoding='utf8') as out_file:
        for line in out_lines:
            out_file.write (line + '\n')

    if file_type is 'b':
        print ('Converted csv file to bib!')
    else:
        print ('Converted bib file to csv!')
    

if __name__ == '__main__':
    # main()
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