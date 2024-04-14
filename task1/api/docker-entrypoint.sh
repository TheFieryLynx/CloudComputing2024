#!/bin/bash

. .venv/bin/activate

uvicorn src.api.app:app --forwarded-allow-ips='*' --host 0.0.0.0