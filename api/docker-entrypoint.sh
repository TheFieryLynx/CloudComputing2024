#!/bin/bash

. .venv/bin/activate

exec uvicorn src.api.app:app --forwarded-allow-ips='*' --host 0.0.0.0