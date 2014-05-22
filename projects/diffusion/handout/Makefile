
pr=main

pdf=${pr}.pdf
ps=${pr}.ps
picps=${pr}-pics.ps
dvi=${pr}.dvi
tex=${pr}.tex
aux=${pr}.aux
out_pdf=output.pdf

all: pstricks pdflatex
	pdflatex ${tex}
#	mv ${pdf} ${out_pdf}

pdflatex:
	pdflatex ${tex}

pstricks:
	latex ${tex}
	dvips -o ${pr}-pics.ps ${dvi}
	ps2pdf ${pr}-pics.ps

bibtex:
	bibtex ${aux}

clean:
	rm -f *.dvi *.ps *.log *.aux *~ *-pics.pdf *.toc *.out

pdflatextwice:
	pdflatex ${tex}
	pdflatex ${tex}


