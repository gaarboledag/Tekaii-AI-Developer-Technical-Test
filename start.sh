#!/bin/bash
echo "Iniciando Docker..."
docker compose up -d
echo "API disponible en: http://localhost:8000"
echo "Documentación en: http://localhost:8000/docs"