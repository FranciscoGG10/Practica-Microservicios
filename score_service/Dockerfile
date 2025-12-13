FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Nota: El CMD cambia solo el puerto según el servicio (8001, 8002, 8003)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]