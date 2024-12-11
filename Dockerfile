# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto para el contenedor
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
