#!/bin/sh
# Si no existen las variables, usa localhost por defecto
AUTH_URL=${AUTH_URL:-"http://localhost:8001"}
GAME_URL=${GAME_URL:-"http://localhost:8002"}
SCORE_URL=${SCORE_URL:-"http://localhost:8003"}

# Escribir el archivo JS
echo "window.env = {" > /usr/share/nginx/html/env-config.js
echo "  AUTH_URL: \"$AUTH_URL\"," >> /usr/share/nginx/html/env-config.js
echo "  GAME_URL: \"$GAME_URL\"," >> /usr/share/nginx/html/env-config.js
echo "  SCORE_URL: \"$SCORE_URL\"" >> /usr/share/nginx/html/env-config.js
echo "};" >> /usr/share/nginx/html/env-config.js

# Ejecutar Nginx
exec "$@"