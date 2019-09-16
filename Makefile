# Useful make commands

test:
	pytest

setup:
	python setup.py sdist bdist_wheel

install:
	pip install -e .

clear:
	find . -name "*.jpeg" -type f -delete

