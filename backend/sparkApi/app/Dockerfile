# Use a imagem oficial do Spark com Python 3
FROM bitnami/spark:latest

# Ajustar permissões e instalar dependências necessárias
USER root
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar os arquivos do projeto
COPY . /app

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências Python
RUN pip3 install -r requirements.txt

# Expor a porta onde o FastAPI será executado
EXPOSE 8000

# Comando para iniciar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
