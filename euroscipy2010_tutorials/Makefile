# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         = a4
PYTHON        = python

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d build/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

# Data to ship with the HTML version
HTML_DATA = \
	data/max-speeds.npy \
	data/cumulative-wind-speed-prediction.py \
	data/sprog-windspeeds.npy \
	data/gumbell-wind-speed-prediction.py \
	data/scipy-interpolation.py \
	data/odeint-introduction.py \
	data/odeint-damped-spring-mass.py \
	data/fftpack-illustration.py

.PHONY: help clean html web pickle htmlhelp latex changes linkcheck zip

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  pickle    to make pickle files (usable by e.g. sphinx-web)"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes   to make an overview over all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"

clean:
	-rm -rf build/*

test:
	nosetests -v --with-doctest --doctest-tests --doctest-extension=rst source/*[a-z].rst source/summary-exercices/*.rst

source/interpolation.png:
	$(PYTHON) data/scipy-interpolation.py

source/odeint-introduction.png:
	$(PYTHON) data/odeint-introduction.py

source/odeint-damped-spring-mass.png:
	$(PYTHON) data/odeint-damped-spring-mass.py

source/fftpack-signals.png:
	$(PYTHON) data/fftpack-illustration.py

source/summary-exercices/cumulative-wind-speed-prediction.png:
	$(PYTHON) data/cumulative-wind-speed-prediction.py

# Generate as well sprog-annual-maxima.png
source/summary-exercices/gumbell-wind-speed-prediction.png:
	$(PYTHON) data/gumbell-wind-speed-prediction.py

sources: source/interpolation.png \
		 source/odeint-introduction.png \
		 source/odeint-damped-spring-mass.png \
		 source/fftpack-signals.png \
		 source/summary-exercices/cumulative-wind-speed-prediction.png \
		 source/summary-exercices/gumbell-wind-speed-prediction.png

html: sources
	mkdir -p build/html build/doctrees
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) build/html
	mkdir -p build/html/data
	cp ${HTML_DATA} build/html/data
	@echo
	@echo "Build finished. The HTML pages are in build/html."

pickle:
	mkdir -p build/pickle build/doctrees
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) build/pickle
	@echo
	@echo "Build finished; now you can process the pickle files or run"
	@echo "  sphinx-web build/pickle"
	@echo "to start the sphinx-web server."

web: pickle

htmlhelp:
	mkdir -p build/htmlhelp build/doctrees
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) build/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in build/htmlhelp."

latex: sources
	mkdir -p build/latex build/doctrees
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) build/latex
	@echo
	@echo "Build finished; the LaTeX files are in build/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	mkdir -p build/changes build/doctrees
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) build/changes
	@echo
	@echo "The overview file is in build/changes."

linkcheck:
	mkdir -p build/linkcheck build/doctrees
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) build/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in build/linkcheck/output.txt."

pdf: latex
	cd build/latex ; make all-pdf ; pdfnup PythonScientific.pdf
	cp build/latex/PythonScientific-2x1.pdf build/PythonScientific.pdf
	#cd build/latex ; make all-pdf ; pdfnup python4science.pdf

zip: html pdf
	mkdir -p build/euroscipy_beginners_lecture_notes ;
	cp -r build/html build/euroscipy_beginners_lecture_notes ;
	cp -r data build/euroscipy_beginners_lecture_notes ;
	cp PythonScientific.pdf build/euroscipy_beginners_lecture_notes;
	zip -r build/euroscipy_beginners_lecture_notes.zip build/euroscipy_beginners_lecture_notes  
