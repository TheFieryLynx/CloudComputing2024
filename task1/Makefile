python_bin := python3
enter_venv := . .venv/bin/activate

compose/up: compose/build
	docker compose up

compose/up/d: compose/build
	docker compose up -d

compose/build:
	docker compose build

compose/stop:
	docker compose stop

compose/down:
	docker compose down

compose/down/full:
	docker compose down -v

local/api/.venv: ./api/pyproject.toml
	$(python_bin) -m venv ./api/.venv
	cd api && $(enter_venv) && poetry install

local/api/run: local/api/.venv
	cd api && ./docker-entrypoint.sh
