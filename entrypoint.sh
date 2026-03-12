#!/bin/bash
set -e

echo ">>> Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo ">>> Aplicando migrações..."
python manage.py migrate --noinput

echo ">>> Criando superusuário admin..."
python manage.py create_admin

echo ">>> Iniciando servidor..."
exec "$@"
