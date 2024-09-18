all:
	pdflatex SujetEntier.tex
	 /usr/share/texlive/texmf-dist/scripts/pythontex/pythontex3.py SujetEntier.pytxcode
	pdflatex SujetEntier.tex 
clear:
	rm -f SujetEntier.*
	rm -rf pythontex-files-SujetEntier
go:
	python3 CreationTest.py

