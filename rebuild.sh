#!/bin/bash
echo "🔄 Reconstruyendo Sistema Kanban..."
docker compose down
docker compose build --no-cache
docker compose up -d
echo "✅ Sistema reconstruido y reiniciado!"
