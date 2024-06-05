# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    libx11-6 \
    libxft2 \
    libxext6 \
    libjpeg-dev \
    libfreetype6 \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6 \
    tk8.6 \
    ghostscript \
    xvfb \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libcairo2 \
    libatspi2.0-0 \
    binutils \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requisitos al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Verificar la instalación de Tkinter
RUN python3 -m tkinter || true

# Definir el comando de inicio
CMD ["sh", "-c", "Xvfb :99 -ac & export DISPLAY=:99 && python ./clientes.py"]
