__all__ = ['bibmanager']

# When extending this package, just place
# a mapping from the key to the module.classname
# here and implement the module in the parsers folder
Parsers = {
    'bibtex': 'bibtexparser.BibTexParser',
    'csv': 'csvparser.CSVParser'
}
