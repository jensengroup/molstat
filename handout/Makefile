
pr=${ARGS}

pdf=${pr}.pdf
ps=${pr}.ps
picps=${pr}-pics.ps
dvi=${pr}.dvi
tex=${pr}.tex
aux=${pr}.aux
out_pdf=output.pdf

# make ARGS="asdf" run

all: pstricks pdflatex
	pdflatex ${tex}


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

