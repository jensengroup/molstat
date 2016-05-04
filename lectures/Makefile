
TEX = xelatex

all: lecture_1.pdf lecture_2.pdf lecture_3.pdf lecture_4.pdf lecture_5.pdf

# $< is the name
%.pdf: %.tex
	$(TEX) $<
	$(TEX) $<

clean:
	rm -f *.dvi *.ps *.log *.aux *~ *-pics.pdf *.toc *.out *.vrb *.snm *.nav
