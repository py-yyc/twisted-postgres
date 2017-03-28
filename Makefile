.PHONY: slides

default: slides

slides:
	python build-slides.py code-slides/[0-9][0-9][0-9][0-9]*.py
