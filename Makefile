.PHONY: setup check run

setup:
	uv sync

check:
	uv run pytest tests/

run:
	uv run python -m app.cli "$(TASK)"
