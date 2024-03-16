python_bin := python3.11
enter_venv := . .venv/bin/activate

compose/up: compose/build
	docker compose up

compose/build: local/api/.venv
	docker compose build

compose/down:
	docker compose down

local/api/.venv: ./api/pyproject.toml
	$(python_bin) -m venv ./api/.venv
	cd api && $(enter_venv) && poetry install

local/api/run: local/api/.venv
	cd api && ./docker-entrypoint.sh
