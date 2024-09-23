.PHONY: check

check:
	pipenv run ruff check

fix:
	pipenv run ruff check --fix