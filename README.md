# Тех. задание
Реализовать RESTFull API сервис, с 3-мя эндпоинтами:
1. Получение всех строк из бд
2. Отдает данные из БД, с возможностью фильтрации по полу, с заданным LIMIT
3. Принимает JSON{id, name, gender}, парсит данные и сохраняет в бд. Необходимо валидировать данные (по типу)

Стек: Python, FastApi, PostgresSQL, pydantic
Столбцы в базе данных: id, name(str), gender(str). 
БД заполнить случайными данными.

## Требования:
1. База данных PostgresSQL. Все запросы должны быть защищены от инъекций.
2. К методам должны быть написаны комментарии на русском языке.
3. Использование Docker(https://www.docker.com/). Сервис должен запускаться
командой docker-compose up
4. Все секретные ключи должны быть вынесены в `.env` файл
5. Данные о бд должны быть вынесены в `.env`
6. На выполнение задания даётся восемь дней

## Как установить
Для работы микросервиса нужен Python версии 
не ниже 3.10 и установленное 
ПО для контейнеризации - [Docker](https://docs.docker.com/engine/install/)

#### Настройка переменных окружения
1. Скопируйте файл .env.dist в .env
2. Заполните .env файл. Пример: 
```yaml
DB_PORT=5634:5432
FASTAPI_PORT=8000:8000

POSTGRES_HOST=db_app
POSTGRES_USER=db_user
POSTGRES_PASSWORD=secret
POSTGRES_DB=guild-of-dev
POSTGRES_PORT=5432
```

#### Создаем образ Dockerfile
```shell
docker build . -t fastapi_app:latest
```
#### Запуск приложения в контейнере Docker
```shell
docker compose up
```
Будут запущенны два контейнера (FastApi и Postgres)
#### Для остановки и удаления контейнера Docker
```shell
docker compose down
```

## End points
### GET
```bash
GET /api/v1/humans/
```
#### Описание
Получение строк из базы данных

#### Параметры запроса
- gender - фильтрация по полу (male или female)
- limit - вернуть определенное количество записей из базы данных (от 1 до 100)

#### Пример ответа
```json
[
    {
        "name": "Alina",
        "gender": "male",
        "id": 1
    },
    {
        "name": "Nikita",
        "gender": "female",
        "id": 2
    },
    {
        "name": "Vladimir",
        "gender": "male",
        "id": 3
    }
]

```
### POST
```bash
POST /api/v1/humans/
```
#### Описание
Принимает JSON{id, name, gender}. Добавляет полученные данные в базу данных.

#### Параметры запроса
нет

#### Пример ответа
```json
{
    "ok": true,
    "human_id": 11
}

```