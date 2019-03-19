#

test:
	pytest

install:
	python setup.py sdist

clear:
	find . --name "*.pyc" -type f -delete
	 
