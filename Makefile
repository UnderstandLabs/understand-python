check:
	poetry run black .
	poetry run isort . 
	poetry run autoflake --in-place --recursive --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables .
	poetry run pflake8 .
	poetry run bandit .
	# poetry run safety check
	poetry run mypy .

ci-check:
	poetry run black --check .
	poetry run isort --check .
	poetry run autoflake --check .
	poetry run pflake8 .
	poetry run bandit .
	# poetry run safety check
	poetry run mypy .

### catch all
%:
	@echo $@
