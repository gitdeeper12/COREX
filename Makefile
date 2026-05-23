# COREX Makefile

.PHONY: help install test clean run lint format docker

help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  test        - Run tests"
	@echo "  clean       - Clean temporary files"
	@echo "  run         - Run example evaluation"
	@echo "  lint        - Run linters"
	@echo "  format      - Format code"
	@echo "  docker      - Build Docker image"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v --cov=corex

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

run:
	python examples/basic_evaluation.py

lint:
	ruff check corex/
	mypy corex/

format:
	black corex/ tests/
	isort corex/ tests/

docker:
	docker build -t corex:latest .
