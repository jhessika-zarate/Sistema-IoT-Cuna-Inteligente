
# Usamos una imagen base oficial de Python
FROM python:3.9-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente al contenedor
COPY . .
EXPOSE 8080
