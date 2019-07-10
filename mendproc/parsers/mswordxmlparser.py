##
## Parser for xml files.
## These are the MS Word XML files that mendeley online exports
##
## @author Daniel J. Finnegan
## @date February 2019

import sys
import os
import xml.sax
import json
from mendproc.parsers.bibparser import _BibParser

## This is the content handler for the data output by Mendeley.
## This is the work horse
class MSWordHandler (xml.sax.ContentHandler):
	def __init__ (self):
		xml.sax.ContentHandler.__init__ (self)
		self.entries = [] # List of bib entries 
		self.current_data_tag = ''
		self.current_author = {} ## Needed as we have a set of authors
		self.authors = []

	def startElement (self, name, attributes):
		self.current_data_tag = name

		if name == 'b:Source':
			self.current_entry = {
				'keywords': '',
				'bibkey': '',
				'type': '',
				'abstract': '',
				'author': '',
				'doi': '',
				'url': '',
				'year': '',
				'title': ''
			}

		if name == 'b:NameList':
			self.authors = []

		if name == 'b:Person':
			self.current_author = {}

	def endElement (self, name):
		self.current_data_tag = ''

		if name == 'b:Person':
			self.authors.append (self.current_author)

		if name == 'b:NameList':
			## Go through the authors and create a single string
			authors = ['' + i['last'] + ', ' + i['first'] + ' and ' for i in self.authors[0:-1]] # Sentinel list comprehension
			authors.append (self.authors[-1]['last'] + ', ' + self.authors[-1]['first']) # Do it for the last entry without the and
			self.current_entry['author'] = ''.join (authors)

		if name == 'b:Source':
			self.entries.append (self.current_entry)


	def characters (self, content):
		if self.current_data_tag == 'b:First':
			self.current_author['first'] = content.strip()

		if self.current_data_tag == 'b:Last':
			self.current_author['last'] = content.strip()

		if self.current_data_tag == 'b:SourceType':
			pass

		if self.current_data_tag == 'b:Title':
			self.current_entry['title'] = content.strip ()

		if self.current_data_tag == 'b:Year':
			self.current_entry['year'] = content.strip ()

		if self.current_data_tag == 'b:First':
			self.current_author['first'] = content.strip ()

		if self.current_data_tag == 'b:Last':
			self.current_author['last'] = content.strip ()

		if self.current_data_tag == 'b:StandardNumber':
			self.current_entry['doi'] = content.strip ()

		if self.current_data_tag == 'b:Tag':
			self.current_entry['bibkey'] = content.strip ()

		if self.current_data_tag == 'b:SourceType':
			self.current_entry['type'] = self._translate_source_type (content.strip ())

	def _translate_source_type (self, source_type):
		if source_type == 'JournalArticle':
			return ('article')

		if source_type == 'ConferenceProceedings':
			return ('inproceedings')

		if source_type == 'Book':
			return ('book')

		return ('misc')

class MSWordXMLParser (_BibParser):
	def __init__ (self, data_type):
		_BibParser.__init__ (self, data_type)
		self.MSWordHandler = MSWordHandler()

	# ## Extend this to escape special characters
	# def _clean_info (self, line):
	# 	clean_info = line.replace ("“", '\"')
	# 	return (clean_info)

	## The main workhorse
	## Its the public facing part of the API
	def _parse_lines (self, lines):
		entry = {}
		entries = []

		## One liner as SAX does all the hard work
		xml.sax.parseString (''.join (lines), self.MSWordHandler)
		return (self.MSWordHandler.entries)

	## Inverse operation of bib2dict
	def _parse_entries (self, entries):
		pass ## Not implemented for now
		return lines