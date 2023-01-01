export SHELL := /bin/bash

test-cov:
	pytest --cov-config=.coveragerc --cov=grplot --cov-report term-missing --cov-report html

test:
	pytest --cov-config=.coveragerc --cov=grplot 

lint:
	flake8 --extend-ignore E501,W291 ./grplot ./tests