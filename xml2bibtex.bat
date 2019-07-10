@rem Converts an xml file into a bibtex file, dumping its keywords into output and creating a file of the same name
@python bib2xyz.py --input-format=xml ^
                   --output-format=bibtex ^
                   --dump-keywords ^
                   --output-dir=output ^
                   --output-file=%~n1.bib ^
                   --cutoff-year=%2 ^
                   --keyword-regex=%3 ^
                   %1