# Django Backend Project

## Установка и запуск

1. Клонируйте репозиторий:

    ```bash
    git clone <ваш_репозиторий>
    ```

2. Перейдите в папку проекта:

    ```bash
    cd <папка_с_проектом>
    ```

3. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

4. Активируйте виртуальное окружение:

     ```bash
     source venv/bin/activate
     ```

5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск Docker контейнера

1. Запустите контейнеры с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

2. После запуска контейнеров, проект будет доступен по адресу: `http://localhost:8000/`.

## Применение миграций

1. Выполните миграции базы данных:

    ```bash
    docker exec -it storage-web-1 python manage.py migrate
    ```

2. Для создания тестовых данных, выполните миграции данных:

    ```bash
    docker exec -it storage-web-1 python manage.py migrate --fake-initial
    ```

3. Теперь можно работать с API.

## Использование API

Для доступа к API используйте следующие конечные точки:

- `GET /api/posts/` — Получение списка постов
- `POST /api/posts/` — Создание нового поста
- `GET /api/posts/<int:pk>/` — Получение поста по ID
- `PUT /api/posts/<int:pk>/` — Обновление поста по ID
- `DELETE /api/posts/<int:pk>/` — Удаление поста по ID

Также доступны следующие модели:

- Комментарии
- Лайки на постах
- Лайки на комментариях

## Документация API

Для просмотра документации используйте Swagger:

- Откройте в браузере: `http://localhost:8000/swagger/`
