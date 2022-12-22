export SHELL := /bin/bash

test:
	pytest

lint:
	flake8 --extend-ignore E501,W291 ./grplot ./tests