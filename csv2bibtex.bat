@rem Converts a bibtex file into a csv, dumping its keywords into output and creating a file of the same name
@python bib2xyz.py --input-format=csv ^
                   --output-format=bibtex ^
                   --dump-keywords ^
                   --output-dir=output ^
                   --output-file=%~n1.bib ^
                   --cutoff-year=%2 ^
                   --keyword-regex=%3 ^
                   %1