##
## Parser for bibtex files
##
## @author Daniel J. Finnegan
## @date February 2019

import os
import re
from mendproc.parsers.bibparser import _BibParser

class BibTexParser (_BibParser):
    def __init__ (self, data_type):
        _BibParser.__init__ (self, data_type)
        self.GENERAL_REGEX_PATTERN = '{((?=[\w\d:{])(.+))}'
        self.CITATION_KEY_PATTERN = '^@(.*){(\S+),'

        ## Note this is not an exhaustive list
        ## There are more; these are just the ones I care about
        self.KEYWORDS_PATTERN = '^keywords'
        self.ABSTRACT_PATTERN = '^abstract'
        self.AUTHOR_PATTERN = '^author'
        self.DOI_PATTERN = '^doi'
        self.YEAR_PATTERN = '^year'
        self.TITLE_PATTERN = '^title'
        self.URL_PATTERN = '^url'

    def _match_pattern (self, pattern, line):
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
    def _parse_lines (self, lines):
        entry = {}
        entries = []

        general_pattern = re.compile (self.GENERAL_REGEX_PATTERN)
        citation_key_pattern = re.compile (self.CITATION_KEY_PATTERN)
        keywords_pattern = re.compile (self.KEYWORDS_PATTERN)
        abstract_pattern = re.compile (self.ABSTRACT_PATTERN)
        author_pattern = re.compile (self.AUTHOR_PATTERN)
        doi_pattern = re.compile (self.DOI_PATTERN)
        url_pattern = re.compile (self.URL_PATTERN)
        year_pattern = re.compile (self.YEAR_PATTERN)
        title_pattern = re.compile (self.TITLE_PATTERN)

        for line in lines:
            stripped_line = line.strip (' \t\n')
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
                    keywords = self._match_pattern (general_pattern, stripped_line)
                    entry['keywords'] = keywords

                elif abstract_pattern.search (stripped_line):
                    abstract = self._match_pattern (general_pattern, stripped_line)
                    entry['abstract'] = abstract

                elif author_pattern.search (stripped_line):
                    author = self._match_pattern (general_pattern, stripped_line)
                    entry['author'] = author

                elif doi_pattern.search (stripped_line):
                    doi = self._match_pattern (general_pattern, stripped_line)
                    entry['doi'] = doi

                elif url_pattern.search (stripped_line):
                    url = self._match_pattern (general_pattern, stripped_line)
                    entry['url'] = url

                elif year_pattern.search (stripped_line):
                    year = self._match_pattern (general_pattern, stripped_line)
                    entry['year'] = year

                elif title_pattern.search (stripped_line):
                    title = self._match_pattern (general_pattern, stripped_line)
                    entry['title'] = title

        ## Don't forget about the sentinel!
        entries.append (entry)
        return (entries)

    ## Inverse operation of bib2dict
    def _parse_entries (self, entries):
        lines = []
        for entry in entries:
            lines = lines = lines + self.__entry2bibstr (entry) # Concatenate the entries

        return lines

    ## Convert an entry into a list of strings
    def __entry2bibstr (self, entry):
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
