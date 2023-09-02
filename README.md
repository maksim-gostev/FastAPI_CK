# FastAPI_CK
FastAPI_CK — это REST API на основе FastAPI для управления задачами и сотрудниками в системе отслеживания задач.
Он использует SQLAlchemy для операций с базой данных и Pydantic для проверки данных.

## Используемые технологии

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Poetry](https://python-poetry.org/)

### Функционал
- `/employeer`, `/employeer/{employeer_id}`: Создание/чтение/обновление сотрудников
- `/tasks`, `/tasks/{task_id}`: Задачи создания/чтения/обновления
- `/employeer/busy_employees/`: Самые занятые сотрудники

## Запуск
1. Создайте файл `.env`: скопируйте содержимое `.env_example` в новый файл `.env` в корневом каталоге проекта. Регулировать
переменные в соответствии с настройками вашей среды.
2. Запустите базу данных Postgres с помощью следующей команды:
    ```bash
    docker-compose up -d
   ```
3. Выполните миграцию. Примените миграцию базы данных с помощью Alembic для настройки схемы базы данных. Запустите следующее
команда:
    ```bash
    alembic upgrade head
    ``` 
4. Запустите приложение FastAPI:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```
