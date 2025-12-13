FROM nginx:alpine

# Copiar HTML
COPY index.html /usr/share/nginx/html/index.html

# Copiar script de configuración y dar permisos
COPY env.sh /docker-entrypoint.d/40-env-config.sh
RUN chmod +x /docker-entrypoint.d/40-env-config.sh

# Nginx Alpine ejecuta automáticamente scripts en /docker-entrypoint.d/ antes de arrancar