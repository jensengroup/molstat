
TEX = xelatex

all: project_presentation.pdf

# $< is the name
%.pdf: %.tex
	$(TEX) $<
	$(TEX) $<


clean:
	rm -f *.dvi *.ps *.log *.aux *~ *-pics.pdf *.toc *.out *.vrb *.snm *.nav
