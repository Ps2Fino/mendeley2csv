##
## Dictionary based bibliography manager
##
## @author Daniel J. Finnegan
## @date February 2019

import importlib
# import difflib
from mendproc.parsers.bibtexparser import BibTexParser
from mendproc.parsers.csvparser import CSVParser
from mendproc import Parsers

## Internal manager over the bib dictionary
class BibManager ():
	def __init__ (self):
		self.entries = []
		self.lines = []

	def add_entry (self):
		self.entries.append (entry)

	def dump_keywords (self, lowercase=True):
		keywords = []
		for entry in self.entries:
			if entry['keywords'] is not '':
				keyword_list = entry['keywords'].split (',')
				for keyword in keyword_list:
					if lowercase:
						keywords.append (keyword.lower ().strip ())
					else:
						keywords.append (keyword.strip ())

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
			modulepath, classname = Parsers[data_type].rsplit ('.', maxsplit=1)
			module = importlib.import_module(modulepath)
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
			modulepath, classname = Parsers[data_type].rsplit ('.', maxsplit=1)
			module = importlib.import_module(modulepath)
			class_ = getattr(module, classname)
			parser = class_(data_type)
		else:
			parser = None

		if parser == None:
			raise ValueError ('Unknown type ' + data_type + '. Cannot parse')
		else:
			self.lines = parser.parse_entries (self.entries)

