#!/bin/bash

# Ждем 10 секунд перед запуском скрипта
sleep 10

# Загружаем переменные из файла .env
source . .env

# Переменные для подключения к базе данных
export PGHOST=$POSTGRES_HOST
export PGPORT=$POSTGRES_PORT
export PGDATABASE=$POSTGRES_DB
export PGUSER=$POSTGRES_USER
export PGPASSWORD=$POSTGRES_PASSWORD


# Создание таблицы
psql -c "CREATE TABLE IF NOT EXISTS humans (id SERIAL PRIMARY KEY, name VARCHAR(255), gender VARCHAR(255));"

# Массив с именами
names=("Olga" "Nikita" "Ivan" "Maria" "Alina" "Vladimir" "Alexander" "Anastasia" "Irina" "Nikolay")

# Генерация случайных данных и заполнение таблицы
for i in {1..50}; do
  name=${names[$RANDOM % ${#names[@]}]}
  gender=$(shuf -e "male" "female" -n 1)
  psql -c "INSERT INTO humans (name, gender) VALUES ('$name', '$gender');"
done

echo "Таблица создана и заполнена случайными данными."

# Команда для запуска приложения FastAPI
uvicorn src.main:app --host 0.0.0.0 --port 8000