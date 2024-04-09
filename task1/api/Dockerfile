FROM python:3.11-slim
LABEL maintainer="Andrew Biryukov <biryukov.andrej2000@ispras.ru>"
WORKDIR /app/

RUN pip3 install poetry
RUN python -m venv .venv

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
COPY ./README.md ./README.md

COPY ./src ./src

RUN . .venv/bin/activate && poetry install

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]