.PHONY: help install install-dev test test-verbose test-coverage test-html test-parallel clean lint format check

help:
	@echo "Available targets:"
	@echo "  install         Install package in production mode"
	@echo "  install-dev     Install package with development dependencies"
	@echo "  test            Run tests"
	@echo "  test-verbose    Run tests with verbose output"
	@echo "  test-coverage   Run tests with coverage report"
	@echo "  test-html       Run tests and generate HTML coverage report"
	@echo "  test-parallel   Run tests in parallel"
	@echo "  clean           Remove build artifacts and cache files"
	@echo "  lint            Run flake8 linter"
	@echo "  format          Format code with black"
	@echo "  check           Run all checks (lint + tests)"

install:
	pip install -e .

install-dev:
	pip install -e .
	pip install -r requirements-test.txt

test:
	pytest

test-verbose:
	pytest -v

test-coverage:
	pytest --cov=grplot --cov-report=term-missing

test-html:
	pytest --cov=grplot --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated in htmlcov/index.html"

test-parallel:
	pytest -n auto

test-unit:
	pytest -m unit

test-integration:
	pytest -m integration

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .tox/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

lint:
	flake8 grplot grplot_seaborn --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 grplot grplot_seaborn --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	black grplot grplot_seaborn tests

check: lint test
