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

class _BibParser ():
    def __init__ (self, data_type='bibtex'):
        self.data_type = data_type

    def parse_lines (self, data_lines):
        return (self._parse_lines (data_lines))

    def parse_entries (self, entries):
        return (self._parse_entries (entries))