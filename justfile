start:
    uv run app/main.py

typecheck:
    uv run ty check

lint:
    uv run ruff check --fix
