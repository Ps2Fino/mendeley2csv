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

import os
import re
import csv
from packages.parsers.bibparser import _BibParser

class CSVParser (_BibParser):
    def __init__ (self, data_type):
        _BibParser.__init__ (self, data_type)

    ## Convert a list of lines in csv format to a dictionary
    def _parse_lines (self, lines):
        entries = []
        csvlines_reader = csv.DictReader (lines, delimiter=',', quotechar='"')
        for row in csvlines_reader:
            entries.append (row)

        return (entries)

    ## Inverse operation of csv2dict
    def _parse_entries (self, entries):
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
            lines.append (self.__entry2csvstr (entry))

        return (lines)

    ## convert an entry into a csv string
    def __entry2csvstr (self, entry):
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

