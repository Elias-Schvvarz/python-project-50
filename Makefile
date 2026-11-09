install:
	uv pip install -e .

lint:
	uv run ruff check .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_code --cov-report xml