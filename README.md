## Запуск

Для запуска Django-приложения выполнить следующее из корня проекта:

```bash
  pip install -r requirements.txt
  python manage.py runserver
```

Для запуска Celery выполнить следующее из корня проекта:
```bash
  redis-server
  celery -A resource_monitor worker -l info
  celery -A resource_monitor beat -l info
```
Для запуска MySQL выполнить следующие команды:
```bash
  CREATE DATABASE resource_monitor_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';
  GRANT ALL PRIVILEGES ON resource_monitor_db.* TO 'user'@'localhost';
  FLUSH PRIVILEGES;
```

Для запуска mock-запросов выполнить следующее из `/mock_responses`:
```bash
  uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

## Использование

Перейти в `localhost:8000/admin`, ввести логин/пароль от суперпользователя: `root:root`.
В `machines` добавить эндпойнты на ручки `mock_responses`.
