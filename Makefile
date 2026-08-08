SHELL := /bin/bash
PY := python
PYTEST := PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest
PRECOMMIT := python -m pre_commit

.PHONY: test lint format typecheck security spell precommit ci clean

test:
	$(PYTEST) tests/ -v

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy tools tests

security:
	@bandit -r tools tests -q || true

spell:
	codespell tools tests *.md

precommit:
	$(PRECOMMIT) run --all-files

ci: lint format typecheck security spell test
	@echo "CI OK"

clean:
	rm -rf .pytest_cache dist build *.egg-info
