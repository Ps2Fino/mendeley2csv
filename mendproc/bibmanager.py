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

import importlib
# import difflib
from nltk import Text
from packages.parsers.bibtexparser import BibTexParser
from packages.parsers.csvparser import CSVParser
from packages import Parsers

## Internal manager over the bib dictionary
class BibManager ():
	def __init__ (self):
		self.entries = []
		self.lines = []

	def add_entry (self):
		self.entries.append (entry)

	def dump_keywords (self):
		## TODO: Process the keywords, merging duplicates
		keywords = []
		for entry in self.entries:
			keyword_list = entry['keywords'].split (',')
			for keyword in keyword_list:
				keywords.append ('\"' + keyword + '\"')

		return (keywords)

	def dump_authors (self):
		authors = []
		for entry in self.entries:
			author_list = entry['author'].split (';')
			for author in author_list:
				authors.append (author)

		return (authors)

	def lines2entries (self, data_lines, data_type='bibtex'):
		if data_type in Parsers:
			modulename, classname = Parsers[data_type].split ('.')
			module = importlib.import_module('packages.parsers.' + modulename)
			class_ = getattr(module, classname)
			parser = class_(data_type)
		else:
			parser = None

		if parser == None:
			raise ValueError ('Unknown type ' + data_type + '. Cannot parse')
		else:
			self.entries = parser.parse_lines (data_lines) ## Otherwise parse the lines into bib entries

	def entries2lines (self, data_type='bibtex'):
		if data_type in Parsers:
			modulename, classname = Parsers[data_type].split ('.')
			module = importlib.import_module('packages.parsers.' + modulename)
			class_ = getattr(module, classname)
			parser = class_(data_type)
		else:
			parser = None

		if parser == None:
			raise ValueError ('Unknown type ' + data_type + '. Cannot parse')
		else:
			self.lines = parser.parse_entries (self.entries)

