# Use uma imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do diretório atual para o diretório de trabalho do container
COPY . .

# Expõe a porta que o Flask usará
EXPOSE 5000

# Define o comando padrão para rodar a aplicação
CMD ["python", "app.py"]