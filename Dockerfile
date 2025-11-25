
FROM python:3.12-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos las dependencias
COPY requirements.txt .

# Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de tu proyecto
COPY . .

# Comando para iniciar la tienda
CMD ["python", "main.py"]