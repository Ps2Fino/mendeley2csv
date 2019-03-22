##
## Parser for CSV files
##
## @author Daniel J. Finnegan
## @date February 2019

import os
import re
import csv
from mendproc.parsers.bibparser import _BibParser

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
		self.__cleanstr(entry['bibkey']),
		self.__cleanstr(entry['author']),
		self.__cleanstr(entry['title']),
		self.__cleanstr(entry['keywords']),
		self.__cleanstr(entry['abstract']),
		self.__cleanstr(entry['year']),
		self.__cleanstr(entry['doi']),
		self.__cleanstr(entry['url']),
		)

		return (csvstr)

	def __cleanstr (self, str_to_clean):
		return (str_to_clean.replace ("\"", '\''))

