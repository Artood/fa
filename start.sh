#!/bin/sh

# Ожидание запуска PostgreSQL
echo "Waiting for PostgreSQL to start..."
while ! nc -z fa_postgres 5432; do   
  sleep 1
done
echo "PostgreSQL started"

# Инициализация Alembic
echo "Checking Alembic migrations..."
if [ -z "$(ls -A alembic/versions 2>/dev/null)" ]; then
    echo "No migrations found, creating initial migration..."
    alembic revision --autogenerate -m "Initial migration"
fi

# Применение миграций
alembic upgrade head

# Запуск FastAPI через Uvicorn
exec uvicorn main:app --host 0.0.0.0 --port 8009
