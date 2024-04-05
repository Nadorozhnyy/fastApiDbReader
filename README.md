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

#### Запуск СУБД Postgresql
```shell
docker run --name guild-of-dev-db -e POSTGRES_USER=db_user -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=guild-of-dev -p 5634:5432 -d postgres
```
