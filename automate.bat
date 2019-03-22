call bibtex2csv.bat audio.bib
call bibtex2csv.bat haptics.bib
call bibtex2csv.bat presence.bib
call bibtex2csv.bat rendering.bib
call bibtex2csv.bat walking.bib

call csv2bibtex.bat output\audio.csv
call csv2bibtex.bat output\haptics.csv
call csv2bibtex.bat output\presence.csv
call csv2bibtex.bat output\rendering.csv
call csv2bibtex.bat output\walking.csv

@del output\audio.csv
@del output\haptics.csv
@del output\presence.csv
@del output\rendering.csv
@del output\walking.csv