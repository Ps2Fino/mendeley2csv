@rem Converts an xml file into a bibtex file, dumping its keywords into output and creating a file of the same name
@python bib2xyz.py --input-format=xml ^
                   --output-format=csv ^
                   --dump-keywords ^
                   --output-dir=output ^
                   --output-file=%~n1.csv ^
                   --cutoff-year=%2 ^
                   --keyword-regex=%3 ^
                   %1