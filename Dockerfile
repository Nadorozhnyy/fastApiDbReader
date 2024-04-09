# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем переменную окружения для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Устанавливаем PostgreSQL и утилиты
RUN apt-get update && apt-get install -y postgresql-client

# Создаем директорию для приложения и устанавливаем рабочую директорию
RUN mkdir /src
WORKDIR /src

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в образ
COPY . /src/

