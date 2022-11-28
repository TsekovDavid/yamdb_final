![example workflow](https://github.com/TsekovDavid/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=blue)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=blue)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=blue)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=blue)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=blue)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=blue)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=blue)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=blue)](https://github.com/features/actions)

# CI/CD для проекта [api_yamdb](https://github.com/TsekovDavid/api_yamdb) 
* автоматический запуск тестов
* обновление образов на Docker Hub
* автоматический деплой на боевой сервер при пуше в главную ветку main
## Workflow
* tests - Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest. Дальнейшие шаги выполнятся только если push был в ветку master или main.
* build_and_push_to_docker_hub - Сборка и пуш образов на Docker Hub
* deploy - Автоматический деплой проекта на боевой сервер из Docker Hub.
* send_message - Отправка уведомления в Telegram


 ### Подготовка:
Отредактируйте файл `nginx/default.conf` и в строке `server_name` впишите IP виртуальной машины (сервера).  
Скопируйте подготовленные файлы `docker-compose.yaml` и `nginx/default.conf` из вашего проекта на сервер:
```
scp docker-compose.yaml <username>@<host>/home/<username>/docker-compose.yaml
sudo mkdir nginx
scp default.conf <username>@<host>/home/<username>/nginx/default.conf
```
### В репозитории проекта перейдите в settings/secrets/actions и создайте:
```
DOCKER_USERNAME - имя пользователя в DockerHub
DOCKER_PASSWORD - пароль пользователя в DockerHub
SERVER_IP - ip-адрес сервера
USER - пользователь
SSH_KEY - приватный ssh-ключ (публичный должен быть на сервере)
SSH_PASSWORD - кодовая фраза для ssh-ключа
DB_ENGINE - django.db.backends.postgresql
DB_NAME - postgres
POSTGRES_USER - postgres
POSTGRES_PASSWORD - postgres
DB_HOST - db
DB_PORT - 5432
SECRET_KEY - секретный ключ приложения django
ALLOWED_HOSTS - список разрешённых адресов
TELEGRAM_TO - id своего телеграм-аккаунта (@userinfobot, команда /start)
TELEGRAM_TOKEN - токен бота (@BotFather, команда /token)
```

## Как развернуть проект локально:
* Склонируйте репозиторий:
```
git clone https://github.com/TsekovDavid/yamdb_final.git 
```
* Создайте виртуальное окружение и активируйте его: 
``` 
python3 -m venv venv
source venv/scripts/activate - windows
. venv/bin/activate - mac
``` 
* Установите зависимости:
```
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt  
```
  
* Перейдите в api_yamdb/ и выполните миграции:
```
python3 manage.py migrate 
```
* Заполните бд:
```
python3 manage.py load_to_database
```
Создайте суперпользователя
```
python manage.py createsuperuser
```
Запустите сервер 
```
python manage.py runserver  
```
  
  
Проект запущен и доступен по адресу [localhost:8000](http://localhost:8000/)
  
Документация API YaMDb доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
