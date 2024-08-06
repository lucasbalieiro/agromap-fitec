#!/bin/bash
pytest --cov="." --cov-report html && \
alembic upgrade heads && \
uvicorn app.main:app --host 0.0.0.0 --reload
