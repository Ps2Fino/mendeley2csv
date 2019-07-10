__all__ = ['bibmanager']

# When extending this package, just place
# a mapping from the key to the module.classname
# here and implement the module in the parsers folder
Parsers = {
    'bibtex': 'mendproc.parsers.bibtexparser.BibTexParser',
    'csv': 'mendproc.parsers.csvparser.CSVParser',
    'xml': 'mendproc.parsers.mswordxmlparser.MSWordXMLParser'
}
