##
## Abstract parser for bib files.
## Declares functions for parsing lines
## into entries and conversely
##
## @author Daniel J. Finnegan
## @date February 2019

class _BibParser ():
    def __init__ (self, data_type='bibtex'):
        self.data_type = data_type

    def parse_lines (self, data_lines):
        return (self._parse_lines (data_lines))

    def parse_entries (self, entries):
        return (self._parse_entries (entries))