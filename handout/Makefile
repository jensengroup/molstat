
TEX=pdflatex

all: exercise_1.pdf exercise_2.pdf exercise_3.pdf exercise_4.pdf exercise_5.pdf

# $< is the name
%.pdf: %.tex
	$(TEX) $<
	$(TEX) $<

clean:
	rm -f *.dvi *.ps *.log *.aux *~ *-pics.pdf *.toc *.out *.vrb *.snm *.nav *.synctex.gz

