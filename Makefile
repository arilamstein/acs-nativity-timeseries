.PHONY: check help

check:
	uv run ruff format .
	uv run ruff check .
	uv run mypy .
	uv run pytest

coverage:
	uv run pytest --cov=acs_nativity --cov-report=term-missing

help:
	@echo "Available commands:"
	@echo "  make check          Run all CI checks (linting, type checks, and tests)"
	@echo "  make coverage       Run tests with coverage summary"
