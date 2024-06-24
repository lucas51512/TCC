FROM openjdk:11-jre-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala Spark
RUN curl -o /tmp/spark-3.1.2-bin-hadoop3.2.tgz \
    https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz \
    && tar -xvzf /tmp/spark-3.1.2-bin-hadoop3.2.tgz -C /opt/ \
    && ln -s /opt/spark-3.1.2-bin-hadoop3.2 /opt/spark

# Configura Spark Home
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

WORKDIR /app

# Copia os arquivos do projeto
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
