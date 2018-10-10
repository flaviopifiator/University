#!/bin/sh
echo "Borrando migraciones..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
echo "Borrando cache..."
find . -path "*/migrations/*.pyc"  -delete
echo "OK"